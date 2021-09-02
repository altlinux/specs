%define        gemname multi_xml

Name:          gem-multi-xml
Version:       0.6.0
Release:       alt2.1
Summary:       A generic swappable back-end for XML parsing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sferik/multi_xml
Vcs:           https://github.com/sferik/multi_xml.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.0 gem(bundler) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_alias_names multi_xml,multi-xml
Obsoletes:     ruby-multi_xml < %EVR
Provides:      ruby-multi_xml = %EVR
Provides:      gem(multi_xml) = 0.6.0


%description
RMagick is an interface between the Ruby programming language and the
ImageMagick image processing library.


%package       -n gem-multi-xml-doc
Version:       0.6.0
Release:       alt2.1
Summary:       A generic swappable back-end for XML parsing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета multi_xml
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(multi_xml) = 0.6.0

%description   -n gem-multi-xml-doc
A generic swappable back-end for XML parsing documentation files.

RMagick is an interface between the Ruby programming language and the
ImageMagick image processing library.

%description   -n gem-multi-xml-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета multi_xml.


%package       -n gem-multi-xml-devel
Version:       0.6.0
Release:       alt2.1
Summary:       A generic swappable back-end for XML parsing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета multi_xml
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(multi_xml) = 0.6.0
Requires:      gem(bundler) >= 1.0 gem(bundler) < 3

%description   -n gem-multi-xml-devel
A generic swappable back-end for XML parsing development package.

RMagick is an interface between the Ruby programming language and the
ImageMagick image processing library.

%description   -n gem-multi-xml-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета multi_xml.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-multi-xml-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-multi-xml-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt2.1
- ! spec

* Thu Aug 01 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt2
- ^ Ruby Policy 2.0

* Mon Feb 04 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus
