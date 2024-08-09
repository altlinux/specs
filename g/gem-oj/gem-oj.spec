%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname oj

Name:          gem-oj
Version:       3.16.4
Release:       alt1
Summary:       A fast JSON parser and Object marshaller as a Ruby gem
License:       MIT
Group:         Development/Ruby
Url:           http://www.ohler.com/oj/
Vcs:           https://github.com/ohler55/oj.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 5
BuildRequires: gem(rake-compiler) >= 0.9
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-minitest) >= 0.13.0
BuildRequires: gem(test-unit) >= 3.0
BuildRequires: gem(bigdecimal) >= 3.0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-minitest) >= 1
BuildConflicts: gem(test-unit) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-minitest >= 0.13.0,rubocop-minitest < 1
Requires:      gem(bigdecimal) >= 3.0
Obsoletes:     ruby-oj < %EVR
Provides:      ruby-oj = %EVR
Provides:      gem(oj) = 3.16.4


%description
Version 3.0 is out! 3.0 provides better json gem and Rails compatibility. It
also provides additional optimization options.


%if_enabled    doc
%package       -n gem-oj-doc
Version:       3.16.4
Release:       alt1
Summary:       A fast JSON parser and Object marshaller as a Ruby gem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета oj
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(oj) = 3.16.4

%description   -n gem-oj-doc
A fast JSON parser and Object marshaller as a Ruby gem documentation
files.

Version 3.0 is out! 3.0 provides better json gem and Rails compatibility. It
also provides additional optimization options.

%description   -n gem-oj-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета oj.
%endif


%if_enabled    devel
%package       -n gem-oj-devel
Version:       3.16.4
Release:       alt1
Summary:       A fast JSON parser and Object marshaller as a Ruby gem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета oj
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(oj) = 3.16.4
Requires:      gem(minitest) >= 5
Requires:      gem(rake-compiler) >= 0.9
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-minitest) >= 0.13.0
Requires:      gem(test-unit) >= 3.0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-minitest) >= 1
Conflicts:     gem(test-unit) >= 4

%description   -n gem-oj-devel
A fast JSON parser and Object marshaller as a Ruby gem development
package.

Version 3.0 is out! 3.0 provides better json gem and Rails compatibility. It
also provides additional optimization options.

%description   -n gem-oj-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета oj.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-oj-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-oj-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Fri Jul 26 2024 Pavel Skrylev <majioa@altlinux.org> 3.16.4-alt1
- ^ 3.13.21 -> 3.16.4

* Wed Sep 21 2022 Pavel Skrylev <majioa@altlinux.org> 3.13.21-alt1
- ^ 3.13.11 -> 3.13.21

* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 3.13.11-alt1
- ^ 3.11.5 -> 3.13.11

* Sat Apr 24 2021 Pavel Skrylev <majioa@altlinux.org> 3.11.5-alt1
- new version 3.11.5

* Tue Apr 07 2020 Pavel Skrylev <majioa@altlinux.org> 3.10.5-alt1.1
- ! spec obsolete/provide pair

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 3.10.5-alt1
- updated (^) 3.9.1 -> 3.10.5
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.9.1-alt1
- updated (^) 3.9.0 -> 3.9.1
- fixed (!) spec according to changelog rules

* Tue Aug 27 2019 Pavel Skrylev <majioa@altlinux.org> 3.9.0-alt1
- updated (^) 3.7.12 -> 3.9.0
- fixed (!) spec

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 3.7.12-alt1
- New version.

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 3.7.9-alt1
- Bump to 3.7.9.
- Use Ruby Policy 2.0.

* Mon Oct 29 2018 Pavel Skrylev <majioa@altlinux.org> 3.7.0-alt1
- new version 3.7.0

* Wed Oct 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.12-alt1
- New version.

* Thu Sep 27 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.11-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.10-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 22 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.3-alt1
- New version.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.2-alt1
- New version.

* Sat May 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version.

* Sat Apr 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.1-alt1
- New version.

* Mon Apr 09 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1.1.M80P.1
- Backport new version to p8 branch.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1.1
- Rebuild with Ruby 2.5.0

* Mon Mar 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- New version.

* Fri Jan 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version.

* Mon Jan 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.10-alt1
- New version.

* Sat Oct 28 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.9-alt1
- New version

* Thu Oct 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.8-alt1
- New version

* Tue Oct 03 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.7-alt1
- New version

* Sat Sep 23 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.6-alt1
- New version

* Wed Sep 20 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.5-alt0.M80P.2
Rebuild with Ruby 2.4.2

* Sat Sep 09 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.5-alt1.1
- Rebuild with Ruby 2.4.1

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.5-alt0.M80P.1
- Backport new version to p8 branch
- Drop obsoleted patch

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.5-alt1
- New version

* Fri Aug 04 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.4-alt1
- New version

* Wed Aug 02 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.3-alt1
- New version

* Wed Jul 12 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.2-alt1
- New version

* Tue Jul 11 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.1-alt1
- New version

* Sun Jul 09 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1
- New version

* Wed Jul 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- New version

* Thu Jun 22 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.0-alt1
- New version

* Mon Jun 19 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.4-alt1
- New version

* Fri Jun 16 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.3-alt0.M80P.1
- Backport new version to p8 branch
- Fix build with old Ruby

* Wed Jun 14 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.3-alt1
- New version

* Tue Jun 13 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.2-alt1
- New version

* Mon Jun 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version

* Sat Jun 03 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.11-alt1
- New version

* Fri May 19 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.9-alt1
- New version

* Wed May 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.8-alt1
- New version

* Thu May 11 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.7-alt1
- New version

* Mon May 08 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.6-alt1
- New version

* Thu May 04 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.5-alt1
- New version

* Tue May 02 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.4-alt1
- New version

* Fri Apr 28 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version

* Wed Apr 26 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- New version

* Tue Apr 25 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version

* Wed Mar 22 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.5-alt1
- New version

* Wed Mar 15 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.3-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.2-alt1
- New version
- Remove ActiveSupportHelper
- Rebuild with new %%ruby_sitearchdir location

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.1-alt1
- new version 2.18.1

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 2.17.4-alt1
- new version 2.17.4

* Tue Jun 02 2015 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt0.M70P.1
- Backport new version to p7 branch

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- Initial build for ALT Linux
