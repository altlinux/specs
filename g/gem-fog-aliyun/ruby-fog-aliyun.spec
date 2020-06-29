%define        pkgname fog-aliyun

Name:          gem-%pkgname
Version:       0.3.13
Release:       alt1
Summary:       Fog provider for aliyun
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-aliyun
Vcs:           https://github.com/fog/fog-aliyun.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
%summary.


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
%ruby_build

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
* Thu Jun 18 2020 Pavel Skrylev <majioa@altlinux.org> 0.3.13-alt1
- > Ruby Policy 2.0
- ^ 0.3.2 -> 0.3.13

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1
- New version.

* Fri Jun 22 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- New version.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus
