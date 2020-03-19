# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname foreman

Name:          gem-%pkgname
Version:       0.87.0
Release:       alt1
Summary:       Process manager for applications with multiple components
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ddollar/foreman
Vcs:           https://github.com/ddollar/foreman.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.


%package       -n %pkgname.rb
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname.rb
Executable file for %gemname gem.

%description   -n %pkgname.rb -l ru_RU.UTF8
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
%ruby_build --use=foreman --alias=foreman.rb

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n %pkgname.rb
%_bindir/%{pkgname}*
%_mandir/%{pkgname}*

%files         doc
%ruby_gemdocdir


%changelog
* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 0.87.0-alt1
- + packaged gem with usage Ruby Policy 2.0
