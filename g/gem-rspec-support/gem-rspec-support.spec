%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rspec-support

Name:          gem-rspec-support
Version:       3.13.1
Release:       alt1
Summary:       Common code needed by the other RSpec gems
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rspec/rspec-support
Vcs:           https://github.com/rspec/rspec-support.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(thread_order) >= 1.1.0
BuildRequires: gem(rake) > 10.0.0
BuildRequires: gem(diff-lcs) >= 1.4.3
BuildRequires: gem(childprocess) >= 3.0.0
BuildRequires: gem(simplecov) >= 0.8
BuildRequires: gem(ffi) >= 1.13.0
BuildConflicts: gem(thread_order) >= 1.2
BuildConflicts: gem(diff-lcs) >= 2
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency json >= 2.3.0,json < 3
%ruby_use_gem_dependency ffi >= 1.15.5,ffi < 2
Obsoletes:     ruby-rspec-support < %EVR
Provides:      ruby-rspec-support = %EVR
Provides:      gem(rspec-support) = 3.13.1


%description
RSpec::Support provides common functionality to RSpec::Core, RSpec::Expectations
and RSpec::Mocks. It is considered suitable for internal use only at this time.


%if_enabled    doc
%package       -n gem-rspec-support-doc
Version:       3.13.1
Release:       alt1
Summary:       Common code needed by the other RSpec gems documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-support
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-support) = 3.13.1

%description   -n gem-rspec-support-doc
Common code needed by the other RSpec gems documentation files.

RSpec::Support provides common functionality to RSpec::Core, RSpec::Expectations
and RSpec::Mocks. It is considered suitable for internal use only at this time.

%description   -n gem-rspec-support-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-support.
%endif


%if_enabled    devel
%package       -n gem-rspec-support-devel
Version:       3.13.1
Release:       alt1
Summary:       Common code needed by the other RSpec gems development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-support
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-support) = 3.13.1
Requires:      gem(thread_order) >= 1.1.0
Requires:      gem(rake) > 10.0.0
Requires:      gem(diff-lcs) >= 1.4.3
Requires:      gem(childprocess) >= 3.0.0
Requires:      gem(simplecov) >= 0.8
Requires:      gem(ffi) >= 1.13.0
Conflicts:     gem(thread_order) >= 1.2
Conflicts:     gem(diff-lcs) >= 2
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(ffi) >= 2
Conflicts:     gem(rubocop) >= 2

%description   -n gem-rspec-support-devel
Common code needed by the other RSpec gems development package.

RSpec::Support provides common functionality to RSpec::Core, RSpec::Expectations
and RSpec::Mocks. It is considered suitable for internal use only at this time.

%description   -n gem-rspec-support-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-support.
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

%if_enabled    doc
%files         -n gem-rspec-support-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rspec-support-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 3.13.1-alt1
- ^ 3.10.2 -> 3.13.1

* Wed May 26 2021 Pavel Skrylev <majioa@altlinux.org> 3.10.2-alt1
- ^ 3.8.0 -> 3.10.2

* Fri Mar 1 2019 Pavel Skrylev <majioa@altlinux.org> 3.8.0-alt2
- Use Ruby Policy 2.0.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jan 31 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt1
- New version.

* Tue Oct 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version

* Fri May 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version

* Wed Mar 08 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- New version

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 3.2.2-alt1
- Initial build for ALT Linux
