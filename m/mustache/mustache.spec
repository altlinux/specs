# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname mustache

Name:          %pkgname
Version:       1.1.1
Release:       alt1
Summary:       Logic-less Ruby templates
License:       MIT
Group:         Development/Ruby
Url:           http://mustache.github.io/
%vcs           https://github.com/mustache/mustache.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:  %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary
Inspired by ctemplate and et, Mustache is a framework-agnostic way to render
logic-free views.

As ctemplates says, "It emphasizes separating logic from presentation: it is
impossible to embed application logic in this template language."


%package       -n gem-%pkgname
Summary:       Library for %gemname gem
Summary(ru_RU.UTF-8): Библиотечные файлы для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-%pkgname
Library for %gemname gem.

%description   -n gem-%pkgname -l ru_RU.UTF8
Библиотечные файлы для %gemname самоцвета.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch
Provides:      %pkgname-doc
Obsoletes:     %pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
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
%_bindir/%{pkgname}*
%_mandir/*

%files         -n gem-%pkgname
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir


%changelog
* Mon Dec 09 2019 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- New version.

* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt2
- Use Ruby Policy 2.0

* Sun Oct 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus
