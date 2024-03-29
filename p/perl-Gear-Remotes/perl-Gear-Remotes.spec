%def_with utils
%define module Gear-Remotes

Name: perl-%module
Version: 0.036
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for quering Gear remotes files
Group: Development/Perl
License: GPLv2+ or Artistic-2.0
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
# TODO: upload to http://search.cpan.org/dist/%module
Url: https://www.altlinux.org/Gear/remotes

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl(Pod/Usage.pm) perl(Pod/Text.pm) perl(RPM/uscan.pm) perl(Gear/Rules.pm) perl(RPM/Source/Editor.pm) perl(RPM/Devscripts/Versort.pm)
Requires: gear perl(Pod/Text.pm)
%if_without utils
Provides: gear-remotes = %version
Provides: gear-remotes-utils = %version
Requires: gear-uupdate
%endif

%description
Perl library and tools to work with .gear/upstream/remotes files.
Gear is a tool for storing, building and maintaining rpm packages
in a git repository for ALT Linux team.

Gear, however, lack means to store essential parts of local configuration,
such as location of upstream VCS it was cloned from or updated.
.gear/upstream/remotes is an extension to Gear to cover this weakness.

See more on [www.altlinux.org/Gear/remotes].

%if_with utils
%package -n gear-remotes-utils
Summary: utilities for manipulating Gear upstream/remotes files
Group: Development/Other
Requires: perl-Gear-Remotes = %EVR
Requires: gear-uupdate
Provides: gear-remotes = %version
Obsoletes: perl-Gear-Remotes < 0.024
Conflicts: perl-Gear-Remotes < 0.024

%description -n gear-remotes-utils
gear-remotes-utils are utils for managing .gear/upstream/remotes file.
.gear/upstream/remotes file is used to save, share and restore local
.git configuration to all maintainers.
%endif

%package -n gear-remotes-batch-watch
Summary: utilities for batch quering for updates from rpm git urls
Group: Development/Other
Requires: perl-Gear-Remotes = %EVR
Requires: /usr/bin/altlinux-find-local-mirror
BuildRequires: perl(Parallel/ForkManager.pm)

%description -n gear-remotes-batch-watch
gear-remotes-batch-watch utils are used for batch quering for updates
from rpm git urls found in VCS: and URL: rpm tags.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

ln -s gr-batch-watch-standalone %buildroot%_bindir/repocop-watch-batch-git-plugin

%files
#doc Changes
#doc README
%perl_vendor_privlib/G*
%if_with utils
%files -n gear-remotes-utils
%endif
%_bindir/gear-remotes-*
%_man1dir/gear-remotes-*

%files -n gear-remotes-batch-watch
%_bindir/gr-batch-*
%_man1dir/gr-batch-*
%_bindir/repocop-watch-*

%changelog
* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 0.036-alt1
- warning if restored url is deprecated

* Thu Jun 30 2022 Igor Vlasenko <viy@altlinux.org> 0.035-alt1
- git+https:// support

* Wed Jun 08 2022 Igor Vlasenko <viy@altlinux.org> 0.034-alt1
- bugfix release

* Mon May 23 2022 Igor Vlasenko <viy@altlinux.org> 0.033-alt1
- new version

* Thu Apr 28 2022 Igor Vlasenko <viy@altlinux.org> 0.032-alt1
- new version

* Wed Mar 16 2022 Igor Vlasenko <viy@altlinux.org> 0.031-alt1
- new version

* Tue Jan 11 2022 Igor Vlasenko <viy@altlinux.org> 0.030-alt1
- new version (closes: #41694)

* Tue Jan 11 2022 Igor Vlasenko <viy@altlinux.org> 0.029-alt1
- new version

* Tue Dec 21 2021 Igor Vlasenko <viy@altlinux.org> 0.028-alt1
- new version

* Mon Dec 06 2021 Igor Vlasenko <viy@altlinux.org> 0.027-alt1
- new version

* Thu Nov 25 2021 Igor Vlasenko <viy@altlinux.org> 0.026-alt1
- new version

* Tue Nov 23 2021 Igor Vlasenko <viy@altlinux.org> 0.025-alt1
- new version
- added gear-remotes-batch-utils

* Fri Nov 05 2021 Igor Vlasenko <viy@altlinux.org> 0.024-alt1
- new version
- added gear-remotes-utils subpackage

* Thu Sep 23 2021 Igor Vlasenko <viy@altlinux.org> 0.023-alt1
- gear-remotes-set-from-spec with VCS: tag support
  instead of old gear-remotes-set-from-spec-comment

* Sat Mar 07 2020 Igor Vlasenko <viy@altlinux.ru> 0.022-alt1
- new version

* Tue Feb 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1
- new version

* Mon Dec 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1
- checks for transform-tag

* Tue Oct 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1
- better usability thanks to grenka@

* Mon Jul 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.018-alt1
- added man pages

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.017-alt1
- check for misspelled remotes/*-tag

* Fri Feb 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- submodules support

* Thu Oct 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- gear-remotes-* utils can now run deep in git tree

* Wed Oct 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- support for git repository comments in spec file

* Wed Oct 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- gear-remotes-save now git add .gear/upstream/remotes

* Wed Feb 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- bugfix release

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- new version

* Thu Jul 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- bugfix release

* Wed Jun 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- added gear-uupdate requires (closes: #32182)

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- proper argument handling in save

* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- added documentation

* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- added gear-remotes-save by cas@
- bugfixes

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- bugfix release

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- new version

* Fri Dec 04 2015 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- added gear-remotes-set-from-url utility

* Mon Nov 30 2015 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- new version

* Wed Jul 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version
