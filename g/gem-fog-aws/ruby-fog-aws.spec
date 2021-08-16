%define        pkgname fog-aws

Name:          gem-%pkgname
Version:       3.7.0
Release:       alt1
Summary:       Module for the 'fog' gem to support Amazon Web Services
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-aws
Vcs:           https://github.com/fog/fog-aws.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
%summary http://aws.amazon.com/.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для %gemname самоцвета


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
* Wed Dec 16 2020 Pavel Skrylev <majioa@altlinux.org> 3.7.0-alt1
- ^ 3.5.2 -> 3.7.0
- ! spec

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 3.5.2-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 1:3.5.2-alt1
- updated (^) 3.5.0 -> 3.5.2

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 1:3.5.0-alt1
- used (>) Ruby Policy 2.0
- updated (^) 2.0.1 -> 3.5.0

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1:2.0.1-alt1
- Use old version for fog-core.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus
