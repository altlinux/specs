%define        pkgname formatador

Name:          ruby-%pkgname
Version:       0.2.5
Release:       alt2
Summary:       STDOUT text formatting
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/geemus/formatador
%vcs           https://github.com/geemus/formatador.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

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
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.5-alt2
- ^ Ruby Policy 2.0

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.5-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus
