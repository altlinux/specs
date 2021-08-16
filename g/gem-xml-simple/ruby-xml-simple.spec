%define        gemname xml-simple

Name:          gem-xml-simple
Version:       1.1.9
Release:       alt1
Summary:       A very simple API for XML processing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/maik/xml-simple
Vcs:           https://github.com/maik/xml-simple.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: rpm-build-ruby
BuildRequires: ruby-tool-rdoc
BuildRequires: gem(rexml) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rexml) >= 0
Obsoletes:     ruby-xml-simple < %EVR
Provides:      ruby-xml-simple = %EVR
Provides:      gem(xml-simple) = 1.1.9


%description
Class XmlSimple offers an easy API to read and write XML. It is a Ruby
translation of Grant McLean's Perl module XML::Simple. Simply put, it
automatically converts XML documents into a Ruby Hash.


%package       -n gem-xml-simple-doc
Version:       1.1.9
Release:       alt1
Summary:       A very simple API for XML processing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета xml-simple
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(xml-simple) = 1.1.9

%description   -n gem-xml-simple-doc
A very simple API for XML processing documentation files.

Class XmlSimple offers an easy API to read and write XML. It is a Ruby
translation of Grant McLean's Perl module XML::Simple. Simply put, it
automatically converts XML documents into a Ruby Hash.

%description   -n gem-xml-simple-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета xml-simple.


%package       -n gem-xml-simple-devel
Version:       1.1.9
Release:       alt1
Summary:       A very simple API for XML processing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета xml-simple
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(xml-simple) = 1.1.9

%description   -n gem-xml-simple-devel
A very simple API for XML processing development package.

Class XmlSimple offers an easy API to read and write XML. It is a Ruby
translation of Grant McLean's Perl module XML::Simple. Simply put, it
automatically converts XML documents into a Ruby Hash.

%description   -n gem-xml-simple-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета xml-simple.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-xml-simple-doc
%ruby_gemdocdir

%files         -n gem-xml-simple-devel


%changelog
* Fri Jul 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.9-alt1
- ^ 1.1.5 -> 1.1.9

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.12-alt1.2
- Rebuild with new Ruby autorequirements.

* Tue Dec 04 2012 Led <led@altlinux.ru> 1.0.12-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sat Jun 27 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.12-alt1
- [1.0.12]

* Mon Mar 31 2008 Sir Raorn <raorn@altlinux.ru> 1.0.11-alt2
- Rebuilt with rpm-build-ruby

* Mon Jan 07 2008 Sir Raorn <raorn@altlinux.ru> 1.0.11-alt1
- Initial build for ALT Linux
