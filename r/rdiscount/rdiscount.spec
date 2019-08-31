%define        pkgname rdiscount

Name:          %pkgname
Version:       2.2.0.1
Release:       alt4
Summary:       Discount (For Ruby) Implementation of John Gruber's Markdown
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           http://dafoster.net/projects/rdiscount/
%vcs           https://github.com/davidfstr/rdiscount.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ronn)

%description
Discount is an implementation of John Gruber's Markdown markup language
in C. It implements all of the language described in the markdown syntax
document and passes the Markdown 1.0 test suite.


%package       -n gem-%pkgname
Summary:       Code for the %gemname gem
Group:         Development/Ruby
Provides:      ruby-%pkgname
Obsoletes:     ruby-%pkgname

%description   -n gem-%pkgname
%summary.

%description   -n gem-%pkgname -l ru_RU.UTF8
Код для самоцвета %gemname.


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


%package       -n gem-%pkgname-devel
Summary:       Development headers files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-devel
Development headers for %gemname gem.

%description   -n gem-%pkgname-devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%_bindir/%pkgname
%_mandir/*

%files         -n gem-%pkgname
%doc README*
%ruby_gemspec
%ruby_gemextdir
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*


%changelog
* Thu Jul 25 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0.1-alt4
! spec
+ ronn gem build dependency

* Wed Apr 10 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0.1-alt3
- Clean up the spec from the dog-nail

* Tue Apr 09 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0.1-alt2.1
- Fix build on i586 with a workaround dog-nail

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0.1-alt2
- Use Ruby Policy 2.0
- Fix spec

* Mon Sep 03 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.0.1-alt1.2
- Rebuild for new Ruby autorequirements.

* Sat Jun 09 2018 Alexey Shabalin <shaba@altlinux.ru> 2.2.0.1-alt1.1
- NMU: rebuild for aarch64

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.0.1-alt1
- Initial build for Sisyphus
