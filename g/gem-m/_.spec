# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname m

Name:          gem-%pkgname
Version:       1.5.1
Release:       alt1
Summary:       A Test::Unit runner that can run tests by line number
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/qrush/m
%vcs           https://github.com/qrush/m.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary. m stands for metal, a better test/unit and minitest test runner that
can run tests by line number.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
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

%files         -n %pkgname
%_bindir/%{pkgname}*

%files         doc
%ruby_gemdocdir


%changelog
* Tue Oct 22 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.1-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
