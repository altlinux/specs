%define  pkgname ruby-ole

Name:          gem-%pkgname
Version:       1.2.12.2
Release:       alt1
Summary:       A library for easy read/write access to OLE compound documents for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/aquasync/ruby-ole
%vcs           https://github.com/aquasync/ruby-ole.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
The ruby-ole library provides a variety of functions primarily for working with
OLE2 structured storage files, such as those produced by Microsoft Office - eg
*.doc, *.msg etc.


%package       -n oletool
Summary:       Oletool is an executable to operate with OLE2 structured storage files from console.
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         System/Base
BuildArch:     noarch

%description   -n oletool
Oletool is an executable to operate with OLE2 structured storage files from
console.

%description   -n oletool -l ru_RU.UTF8
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

%files         -n oletool
%_bindir/oletool

%files         doc
%ruby_gemdocdir

%changelog
* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.12.2-alt1
- Bump to 1.2.12.2
- Use Ruby Policy 2.0

* Wed Dec 19 2018 Pavel Skrylev <majioa@altlinux.org> 1.2.12.1-alt1
- Initial build for Sisyphus bumped to 1.2.12.1.
