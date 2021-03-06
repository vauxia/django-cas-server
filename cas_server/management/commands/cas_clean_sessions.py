# -*- coding: utf-8 -*-
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License version 3 for
# more details.
#
# You should have received a copy of the GNU General Public License version 3
# along with this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# (c) 2016 Valentin Samir
"""Clean deleted sessions management command"""
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _

from ... import models


class Command(BaseCommand):
    """Clean deleted sessions"""
    args = ''
    help = _(u"Clean deleted sessions")

    def handle(self, *args, **options):
        models.User.clean_deleted_sessions()
        models.NewVersionWarning.send_mails()
