%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname libyajl2

Name:          gem-libyajl2
Version:       2.1.0.14.2
Release:       alt0.1
Summary:       gem to install the libyajl2 c-library for distributions which do not have it
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/libyajl2-gem
Vcs:           https://github.com/chef/libyajl2-gem.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake libruby-devel
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(ffi) >= 1.9
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rspec) >= 0
BuildConflicts: gem(ffi) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      libyajl2 = %EVR
Provides:      gem(libyajl2) = 2.1.0.14.2

%ruby_use_gem_version libyajl2:2.1.0.14.2

%description
gem to install the libyajl2 c-library for distributions which do not have it.


%if_enabled    doc
%package       -n gem-libyajl2-doc
Version:       2.1.0.14.2
Release:       alt0.1
Summary:       gem to install the libyajl2 c-library for distributions which do not have it documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета libyajl2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(libyajl2) = 2.1.0.14.2

%description   -n gem-libyajl2-doc
gem to install the libyajl2 c-library for distributions which do not have it
documentation files.

%description   -n gem-libyajl2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета libyajl2.
%endif


%if_enabled    devel
%package       -n gem-libyajl2-devel
Version:       2.1.0.14.2
Release:       alt0.1
Summary:       gem to install the libyajl2 c-library for distributions which do not have it development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета libyajl2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(libyajl2) = 2.1.0.14.2

%description   -n gem-libyajl2-devel
gem to install the libyajl2 c-library for distributions which do not have it
development package.

%description   -n gem-libyajl2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета libyajl2.
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
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-libyajl2-doc
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-libyajl2-devel
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%endif


%changelog
* Tue Aug 11 2026 Pavel Skrylev <majioa@altlinux.org> 2.1.0.14.2-alt0.1
- ^ 2.1.0p2 -> 2.1.0p14.2
- * feature to support system ruby libyajl2

* Wed Feb 14 2024 Pavel Skrylev <majioa@altlinux.org> 2.1.0.2-alt1
- ^ 2.1.0 -> 2.1.0p2

* Mon Oct 11 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt2
- + fix to extconf.rb allowing to use system variable without pass arg to ENV
- ! spec

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 1.2.0 -> 2.1.0

* Tue Feb 05 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- Initial build to ALT of 1.2.0 with usage of Ruby Policy 2.0.
