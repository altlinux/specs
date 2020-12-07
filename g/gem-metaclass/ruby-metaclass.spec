%define        pkgname metaclass

Name:          gem-%pkgname
Version:       0.0.4.1
Release:       alt1
Summary:       Adds a metaclass method to all Ruby objects
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/floehopper/metaclass
Vcs:           https://github.com/floehopper/metaclass.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Adds a __metaclass__ method to all Ruby objects.


%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --use=%gemname --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 0.0.4.1-alt1
- ^ 0.0.4 -> 0.0.4post

* Thu Aug 01 2019 Pavel Skrylev <majioa@altlinux.org> 0.0.4-alt2
- > Ruby Policy 2.0

* Mon Aug 20 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.4-alt1
- Initial build for Sisyphus
