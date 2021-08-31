%define        gemname mixlib-versioning

Name:          gem-mixlib-versioning
Version:       1.2.15
Release:       alt1
Summary:       General purpose Ruby library that allows you to parse, compare, and manipulate version strings in multiple formats
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/mixlib-versioning
Vcs:           https://github.com/chef/mixlib-versioning.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-mixlib-versioning < %EVR
Provides:      ruby-mixlib-versioning = %EVR
Provides:      gem(mixlib-versioning) = 1.2.15


%description
Versioning is hard! mixlib-versioning is a general Ruby library that allows you
to parse, compare and manipulate version numbers in multiple formats. Currently
the following version string formats are supported:
* SemVer 2.0.0
* Opscode SemVer
* Rubygems
* Git Describe
* SemVer Partial

%package       -n gem-mixlib-versioning-doc
Version:       1.2.15
Release:       alt1
Summary:       General purpose Ruby library that allows you to parse, compare, and manipulate version strings in multiple formats documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mixlib-versioning
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mixlib-versioning) = 1.2.15

%description   -n gem-mixlib-versioning-doc
General purpose Ruby library that allows you to parse, compare, and manipulate
version strings in multiple formats documentation files.

Versioning is hard! mixlib-versioning is a general Ruby library that allows you
to parse, compare and manipulate version numbers in multiple formats. Currently
the following version string formats are supported:
* SemVer 2.0.0
* Opscode SemVer
* Rubygems
* Git Describe
* SemVer Partial

%description   -n gem-mixlib-versioning-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mixlib-versioning.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-mixlib-versioning-doc
%ruby_gemdocdir


%changelog
* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.15-alt1
- ^ 1.2.6 -> 1.2.15

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.6-alt1
- New version.

* Mon Aug 27 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Sat Nov 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.3-alt1
- New version

* Sun Sep 24 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus
