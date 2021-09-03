%define        gemname ruby-ole

Name:          gem-ruby-ole
Version:       1.2.12.2
Release:       alt1.1
Summary:       A library for easy read/write access to OLE compound documents for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/aquasync/ruby-ole
Vcs:           https://github.com/aquasync/ruby-ole.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(ruby-ole) = 1.2.12.2


%description
The ruby-ole library provides a variety of functions primarily for working with
OLE2 structured storage files, such as those produced by Microsoft Office -
eg *.doc, *.msg etc.


%package       -n oletool
Version:       1.2.12.2
Release:       alt1.1
Summary:       A library for easy read/write access to OLE compound documents for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ruby-ole
Group:         System/Base
BuildArch:     noarch

Requires:      gem(ruby-ole) = 1.2.12.2

%description   -n oletool
A library for easy read/write access to OLE compound documents for Ruby
executable(s).

The ruby-ole library provides a variety of functions primarily for working with
OLE2 structured storage files, such as those produced by Microsoft Office -
eg *.doc, *.msg etc.

%description   -n oletool -l ru_RU.UTF-8
Исполнямка для самоцвета ruby-ole.


%package       -n gem-ruby-ole-doc
Version:       1.2.12.2
Release:       alt1.1
Summary:       A library for easy read/write access to OLE compound documents for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-ole
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-ole) = 1.2.12.2

%description   -n gem-ruby-ole-doc
A library for easy read/write access to OLE compound documents for Ruby
documentation files.

The ruby-ole library provides a variety of functions primarily for working with
OLE2 structured storage files, such as those produced by Microsoft Office -
eg *.doc, *.msg etc.

%description   -n gem-ruby-ole-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-ole.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n oletool
%doc README.rdoc
%_bindir/oletool

%files         -n gem-ruby-ole-doc
%doc README.rdoc
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.12.2-alt1.1
- ! spec

* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.12.2-alt1
- Bump to 1.2.12.2
- Use Ruby Policy 2.0

* Wed Dec 19 2018 Pavel Skrylev <majioa@altlinux.org> 1.2.12.1-alt1
- Initial build for Sisyphus bumped to 1.2.12.1.
