%define        gemname asciidoctor

Name:          gem-asciidoctor
Version:       2.0.16
Release:       alt1
Summary:       A fast text processor and publishing toolchain for converting AsciiDoc content to different formats
License:       MIT
Group:         Documentation
Url:           https://github.com/asciidoctor/asciidoctor
Vcs:           https://github.com/asciidoctor/asciidoctor.git
Packager:      Gordeev Mikhail <obirvalger@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(concurrent-ruby) >= 1.1.0 gem(concurrent-ruby) < 1.2
# BuildRequires: gem(cucumber) >= 3.1.0 gem(cucumber) < 3.2
BuildRequires: gem(erubi) >= 1.10.0 gem(erubi) < 1.11
BuildRequires: gem(haml) >= 5.2.0 gem(haml) < 5.3
BuildRequires: gem(minitest) >= 5.14.0 gem(minitest) < 6
BuildRequires: gem(nokogiri) >= 1.10.0 gem(nokogiri) < 2
BuildRequires: gem(rake) >= 12.3.0 gem(rake) < 14
BuildRequires: gem(slim) >= 4.1.0 gem(slim) < 4.2
BuildRequires: gem(tilt) >= 2.0.0 gem(tilt) < 2.1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 1.11.1,rake < 2
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(asciidoctor) = 2.0.16


%description
Asciidoctor is a fast text processor and publishing toolchain for converting
AsciiDoc content to HTML5, DocBook 5 (or 4.5) and other formats.


%package       -n asciidoctor
Version:       2.0.16
Release:       alt1
Summary:       A fast text processor and publishing toolchain for converting AsciiDoc content to different formats executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета asciidoctor
Group:         Other
BuildArch:     noarch

Requires:      gem(asciidoctor) = 2.0.16

%description   -n asciidoctor
A fast text processor and publishing toolchain for converting AsciiDoc content
to different formats executable(s).

Asciidoctor is a fast text processor and publishing toolchain for converting
AsciiDoc content to HTML5, DocBook 5 (or 4.5) and other formats.

%description   -n asciidoctor -l ru_RU.UTF-8
Исполнямка для самоцвета asciidoctor.


%package       -n gem-asciidoctor-doc
Version:       2.0.16
Release:       alt1
Summary:       A fast text processor and publishing toolchain for converting AsciiDoc content to different formats documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета asciidoctor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(asciidoctor) = 2.0.16
Obsoletes:     asciidoctor-doc
Provides:      asciidoctor-doc

%description   -n gem-asciidoctor-doc
A fast text processor and publishing toolchain for converting AsciiDoc content
to different formats documentation files.

Asciidoctor is a fast text processor and publishing toolchain for converting
AsciiDoc content to HTML5, DocBook 5 (or 4.5) and other formats.

%description   -n gem-asciidoctor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета asciidoctor.


%package       -n gem-asciidoctor-devel
Version:       2.0.16
Release:       alt1
Summary:       A fast text processor and publishing toolchain for converting AsciiDoc content to different formats development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета asciidoctor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(asciidoctor) = 2.0.16
Requires:      gem(concurrent-ruby) >= 1.1.0 gem(concurrent-ruby) < 1.2
# Requires:      gem(cucumber) >= 3.1.0 gem(cucumber) < 3.2
Requires:      gem(erubi) >= 1.10.0 gem(erubi) < 1.11
Requires:      gem(haml) >= 5.2.0 gem(haml) < 5.3
Requires:      gem(minitest) >= 5.14.0 gem(minitest) < 6
Requires:      gem(nokogiri) >= 1.10.0 gem(nokogiri) < 2
Requires:      gem(rake) >= 12.3.0 gem(rake) < 14
Requires:      gem(slim) >= 4.1.0 gem(slim) < 4.2
Requires:      gem(tilt) >= 2.0.0 gem(tilt) < 2.1

%description   -n gem-asciidoctor-devel
A fast text processor and publishing toolchain for converting AsciiDoc content
to different formats development package.

Asciidoctor is a fast text processor and publishing toolchain for converting
AsciiDoc content to HTML5, DocBook 5 (or 4.5) and other formats.

%description   -n gem-asciidoctor-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета asciidoctor.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.adoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n asciidoctor
%doc README.adoc
%_bindir/asciidoctor

%files         -n gem-asciidoctor-doc
%doc README.adoc
%ruby_gemdocdir

%files         -n gem-asciidoctor-devel
%doc README.adoc


%changelog
* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.16-alt1
- ^ 2.0.10 -> 2.0.16

* Thu Jun 20 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.10-alt1
- Use Ruby Policy 2.0
- Bump to 2.0.10

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.7.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 21 2018 Grigory Ustinov <grenka@altlinux.org> 1.5.7.1-alt1
- Build new version.

* Thu Aug 03 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.6.1-alt1
- Initial build for Sisyphus
