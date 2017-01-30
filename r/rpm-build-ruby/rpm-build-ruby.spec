%def_disable check

Name: rpm-build-ruby
Epoch: 1
Version: 0.2.3
Release: alt1
Summary: RPM helper scripts to calculate Ruby dependencies
License: GPLv2
Group: Development/Ruby
Source: %name-%version.tar
BuildArch: noarch
Requires: ruby >= 1.9
Conflicts: rpm-build <= 4.0.4-alt24
AutoReq: yes,noruby
Requires: ruby >= 1.9
Requires: ruby-stdlibs >= 1.9
Requires: %_bindir/rdoc
Requires: %_bindir/rake
Requires: rpm-macros-ruby = %epoch:%version-%release
Requires: ruby-test-unit = %epoch:%version-%release

%{!?_disable_check:BuildRequires: ruby >= 1.9 ruby-stdlibs >= 1.9}

%description
These herlper scripts will look at ruby source files in your package, and will
use this information to generate automatic Requires and Provides tags for the
package.

%package -n rpm-macros-ruby
Summary: rpm macros for Ruby packages
Group: Development/Ruby

%description -n rpm-macros-ruby
rpm macros for Ruby packages.

%package -n ruby-test-unit
Summary: Utility testrb for testing Ruby packages
Group: Development/Ruby
Requires: rake

%description -n ruby-test-unit
Utility testrb for testing Ruby packages.

%prep
%setup -q

%install
install -d -m 0755 %buildroot{%_rpmlibdir,%_rpmmacrosdir}
install -p -m 0755 ruby.{req,prov}* %buildroot%_rpmlibdir/
install -p -m 0644 rubyreq.rb %buildroot%_rpmlibdir/
install -p -m 0644 ruby.macros %buildroot%_rpmmacrosdir/ruby
install -p -m 0644 ruby.env %buildroot%_rpmmacrosdir/
install -D -m 0755 testrb %buildroot%_bindir/testrb

%check
./test.sh

%files
%lang(ru) %doc README.ru
%_rpmlibdir/ruby*
%_rpmmacrosdir/ruby.env

%files -n rpm-macros-ruby
%_rpmmacrosdir/ruby

%files -n ruby-test-unit
%_bindir/testrb

%changelog
* Mon Jan 30 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.2.3-alt1
- NMU: added rpm-macros-ruby

* Thu Jan 26 2017 Denis Medvedev <nbr@altlinux.org> 1:0.2.2-alt2
- Skip include in dependencies search

* Thu Jan 26 2017 Denis Medvedev <nbr@altlinux.org> 1:0.2.2-alt1
- Added provides based on "load" in addition to "require"

* Tue Oct 25 2016 Andrey Cherepanov <cas@altlinux.org> 1:0.2.1-alt1
- Support requires defined in double quotes in addition to single quotes

* Fri Oct 07 2016 Denis Medvedev <nbr@altlinux.org> 1:0.2.0-alt1
- Requires check changed to bash script instead of ruby

* Fri Oct 07 2016 Denis Medvedev <nbr@altlinux.org> 1:0.1.6-alt1
- Removed dependency to obsolete rubynodes checks

* Thu Oct 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.1.5-alt2
- Set to catch any errors and notice them: %%_ruby_req_method strict.

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 1:0.1.5-alt1
- Create subpackage ruby-test-unit with only rewritten testrb utility.
  Test::Unit module now is a part of Ruby.

* Wed Sep 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.1.4.1-alt1
- Tiny cleanup which is expected to have no noticeable effect:
  + more reliable failing in the shell scripts
    (set -o pipefail; set -eC).
  + .prov: normalize paths before any analysis (and not in the middle).

* Mon Sep 12 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.1.4-alt1
- ruby.prov: added a new case: std arch-independent gems
  (those included in the ruby package itself).

* Thu Mar 13 2014 Led <led@altlinux.ru> 1:0.1.3-alt1
- 0.1.3:
  + ruby.macros: fix %%ruby_ri_sitedir macro

* Wed Dec 12 2012 Led <led@altlinux.ru> 1:0.1.2-alt4
- removed temp symlink

* Wed Dec 12 2012 Led <led@altlinux.ru> 1:0.1.2-alt3
- temporarily added symlink for rebuild ruby

* Sun Dec 09 2012 Led <led@altlinux.ru> 1:0.1.2-alt2
- added requires of %%_bindir/testrb and %%_bindir/rake

* Sat Dec 08 2012 Led <led@altlinux.ru> 1:0.1.2-alt1
- 0.1.2:
  + cleaned up
  + dropped ruby 1.8 support
- cleaned up spec
- updated Requires
- added README.ru
- disabled check

* Fri Apr 08 2011 Timur Aitov <timonbl4@altlinux.org> 1:0.1.1-alt1
- Supported both 1.8.7 and 1.9.2 versions of ruby
- Make difference between 1.8 and 1.9

* Wed Sep 09 2009 Alexey I. Froloff <raorn@altlinux.org> 1:0.1.0-alt2
- Tests moved to %%check section (bootstrap-friendly)

* Mon Jul 06 2009 Alexey I. Froloff <raorn@altlinux.org> 1:0.1.0-alt1
- Updated for ruby 1.9
- Fixed typo in description (closes: #20624)
- Stop processing on syntax error
- Macros moved to %%_rpmmacrosdir

* Sat Nov 01 2008 Sir Raorn <raorn@altlinux.ru> 1:0.0.4-alt1
- Parser rewritten without recursion (Kirill A. Shutemov)

* Sun Aug 31 2008 Sir Raorn <raorn@altlinux.ru> 1:0.0.3-alt1
- Strip '.rb' extension from requires/provides to reduce apt
  cache size
- Process "weak provides" for *.so modules too
- Use files.req mechanism for directory requires (needs recent
  libruby)
- New macros:
  + %%update_setup_rb: update setup.rb script from ruby-tool-setup package
  + %%ruby_test_unit: run tests with testrb script

* Wed Apr 02 2008 Sir Raorn <raorn@altlinux.ru> 1:0.0.2-alt1
- "class << <var>" block support (kas@)

* Fri Mar 28 2008 Sir Raorn <raorn@altlinux.ru> 1:0.0.1-alt1
- Initial build, based on rpm-build-perl

