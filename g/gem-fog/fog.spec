%define        pkgname fog

Name:          gem-%pkgname
Version:       2.2.0
Release:       alt2
Summary:       The Ruby cloud services library
License:       MIT
Group:         Development/Other
Url:           http://fog.io
Vcs:           https://github.com/fog/fog.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         2.2.0.patch
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%gem_replace_version fog-brightbox ~> 1.0

%description
fog is the Ruby cloud services library, top to bottom:

- Collections provide a simplified interface, making clouds easier to
  work with and switch between.
- Requests allow power users to get the most out of the features of each
  individual cloud.
- Mocks make testing and integrating a breeze.


%package       -n %pkgname
Summary:       %summary
Group:         Development/Other
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch
Provides:      fog-doc
Obsoletes:     fog-doc

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup
%patch -p1

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n %pkgname
%doc README*
%_bindir/%pkgname

%files         doc
%ruby_gemdocdir


%changelog
* Wed Jun 17 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt2
- ! require lib when runnung the executable (closes #38607)
- ! spec tags and syntax

* Mon Jun 24 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- > Ruby Policy 2.0
- ^ 2.1.0 -> 2.2.0

* Tue Nov 13 2018 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- Bump to 2.1.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed May 23 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
