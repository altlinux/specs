%define        gemname asciidoctor

Name:          gem-asciidoctor
Version:       2.0.18
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
%if_with check
BuildRequires: gem(concurrent-ruby) >= 1.1.0
BuildRequires: gem(cucumber) >= 3.1.0
BuildRequires: gem(erubi) >= 1.10.0
BuildRequires: gem(haml) >= 5.2.0
BuildRequires: gem(minitest) >= 5.14.0
BuildRequires: gem(nokogiri) >= 1.10.0
BuildRequires: gem(rake) >= 12.3.0
BuildRequires: gem(slim) >= 4.1.0
BuildRequires: gem(tilt) >= 2.0.0
BuildRequires: gem(asciimath) >= 2.0
BuildRequires: gem(coderay) >= 1.1.0
BuildRequires: gem(net-ftp) >= 0
BuildRequires: gem(open-uri-cached) >= 1.0.0
BuildRequires: gem(rouge) >= 3.0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(yard-tomdoc) >= 0
BuildRequires: gem(simplecov) >= 0.16.0
BuildConflicts: gem(concurrent-ruby) >= 1.2
BuildConflicts: gem(cucumber) >= 3.2
BuildConflicts: gem(erubi) >= 1.11
BuildConflicts: gem(haml) >= 5.3
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(nokogiri) >= 1.11
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(slim) >= 4.2
BuildConflicts: gem(tilt) >= 2.1
BuildConflicts: gem(asciimath) >= 3
BuildConflicts: gem(coderay) >= 1.2
BuildConflicts: gem(open-uri-cached) >= 1.1
BuildConflicts: gem(rouge) >= 4
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Provides:      gem(asciidoctor) = 2.0.18


%description
Asciidoctor is a fast text processor and publishing toolchain for converting
AsciiDoc content to HTML5, DocBook 5 (or 4.5) and other formats.


%package       -n asciidoctor
Version:       2.0.18
Release:       alt1
Summary:       A fast text processor and publishing toolchain for converting AsciiDoc content to different formats executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета asciidoctor
Group:         Other
BuildArch:     noarch

Requires:      gem(asciidoctor) = 2.0.18

%description   -n asciidoctor
A fast text processor and publishing toolchain for converting AsciiDoc content
to different formats executable(s).

Asciidoctor is a fast text processor and publishing toolchain for converting
AsciiDoc content to HTML5, DocBook 5 (or 4.5) and other formats.

%description   -n asciidoctor -l ru_RU.UTF-8
Исполнямка для самоцвета asciidoctor.


%package       -n gem-asciidoctor-doc
Version:       2.0.18
Release:       alt1
Summary:       A fast text processor and publishing toolchain for converting AsciiDoc content to different formats documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета asciidoctor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(asciidoctor) = 2.0.18
Obsoletes:     asciidoctor-doc
Provides:      asciidoctor-doc

%description   -n gem-asciidoctor-doc
A fast text processor and publishing toolchain for converting AsciiDoc content
to different formats documentation files.

Asciidoctor is a fast text processor and publishing toolchain for converting
AsciiDoc content to HTML5, DocBook 5 (or 4.5) and other formats.

%description   -n gem-asciidoctor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета asciidoctor.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README-de.adoc README-fr.adoc README-jp.adoc README-zh_CN.adoc README.adoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n asciidoctor
%doc README-de.adoc README-fr.adoc README-jp.adoc README-zh_CN.adoc README.adoc
%_bindir/asciidoctor

%files         -n gem-asciidoctor-doc
%doc README-de.adoc README-fr.adoc README-jp.adoc README-zh_CN.adoc README.adoc
%ruby_gemdocdir


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 2.0.18-alt1
- ^ 2.0.16 -> 2.0.18 (no devel)

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
