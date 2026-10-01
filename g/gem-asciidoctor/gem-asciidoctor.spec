%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname asciidoctor

Name:          gem-asciidoctor
Version:       2.0.26
Release:       alt1.1
Summary:       A fast text processor and publishing toolchain for converting AsciiDoc content to different formats
License:       MIT
Group:         Documentation
Url:           https://github.com/asciidoctor/asciidoctor
Vcs:           https://github.com/asciidoctor/asciidoctor.git
Packager:      Gordeev Mikhail <obirvalger@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby rake setup-rb
%if_enabled check
BuildRequires: gem(asciimath) >= 2.0
BuildRequires: gem(coderay) >= 1.1.0
BuildRequires: gem(concurrent-ruby) >= 1.1.0
BuildRequires: gem(cucumber) >= 3.1.0
BuildRequires: gem(erubi) >= 1.10.0
BuildRequires: gem(haml) >= 6.1.1
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(net-ftp) >= 0
BuildRequires: gem(nokogiri) >= 1.13.0
BuildRequires: gem(open-uri-cached) >= 1.0.0
BuildRequires: gem(rake) >= 12.3.0
BuildRequires: gem(rouge) >= 3.0
BuildRequires: gem(slim) >= 4.1.0
BuildRequires: gem(tilt) >= 2.0.0
BuildConflicts: gem(asciimath) >= 3
BuildConflicts: gem(coderay) >= 1.2
BuildConflicts: gem(concurrent-ruby) >= 1.2
BuildConflicts: gem(cucumber) >= 3.2
BuildConflicts: gem(erubi) >= 1.11
BuildConflicts: gem(haml) >= 7
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(nokogiri) >= 1.14
BuildConflicts: gem(open-uri-cached) >= 1.1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rouge) >= 4
BuildConflicts: gem(slim) >= 4.2
BuildConflicts: gem(tilt) >= 2.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency haml >= 6.1.1,haml < 7
Provides:      gem(asciidoctor) = 2.0.26

%description
Asciidoctor is a fast text processor and publishing toolchain for converting
AsciiDoc content to HTML5, DocBook 5 (or 4.5) and other formats.


%package       -n asciidoctor
Version:       2.0.26
Release:       alt1.1
Summary:       A fast text processor and publishing toolchain for converting AsciiDoc content to different formats executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета asciidoctor
Group:         Other
BuildArch:     noarch

Requires:      ruby
Requires:      gem(asciidoctor) = 2.0.26

%description   -n asciidoctor
A fast text processor and publishing toolchain for converting AsciiDoc content
to different formats executable(s).

Asciidoctor is a fast text processor and publishing toolchain for converting
AsciiDoc content to HTML5, DocBook 5 (or 4.5) and other formats.

%description   -n asciidoctor -l ru_RU.UTF-8
Исполнямка для самоцвета asciidoctor.


%if_enabled    doc
%package       -n gem-asciidoctor-doc
Version:       2.0.26
Release:       alt1.1
Summary:       A fast text processor and publishing toolchain for converting AsciiDoc content to different formats documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета asciidoctor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(asciidoctor) = 2.0.26
Obsoletes:     asciidoctor-doc < %EVR
Provides:      asciidoctor-doc = %EVR

%description   -n gem-asciidoctor-doc
A fast text processor and publishing toolchain for converting AsciiDoc content
to different formats documentation files.

Asciidoctor is a fast text processor and publishing toolchain for converting
AsciiDoc content to HTML5, DocBook 5 (or 4.5) and other formats.

%description   -n gem-asciidoctor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета asciidoctor.
%endif


%if_enabled    devel
%package       -n gem-asciidoctor-devel
Version:       2.0.26
Release:       alt1.1
Summary:       A fast text processor and publishing toolchain for converting AsciiDoc content to different formats development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета asciidoctor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(asciidoctor) = 2.0.26
Requires:      gem(concurrent-ruby) >= 1.1.0
Requires:      gem(cucumber) >= 3.1.0
Requires:      gem(erubi) >= 1.10.0
Requires:      gem(haml) >= 6.1.1
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(nokogiri) >= 1.13.0
Requires:      gem(rake) >= 12.3.0
Requires:      gem(slim) >= 4.1.0
Requires:      gem(tilt) >= 2.0.0
Conflicts:     gem(concurrent-ruby) >= 1.2
Conflicts:     gem(cucumber) >= 3.2
Conflicts:     gem(erubi) >= 1.11
Conflicts:     gem(haml) >= 7
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(nokogiri) >= 1.14
Conflicts:     gem(rake) >= 14
Conflicts:     gem(slim) >= 4.2
Conflicts:     gem(tilt) >= 2.1

%description   -n gem-asciidoctor-devel
A fast text processor and publishing toolchain for converting AsciiDoc content
to different formats development package.

Asciidoctor is a fast text processor and publishing toolchain for converting
AsciiDoc content to HTML5, DocBook 5 (or 4.5) and other formats.

%description   -n gem-asciidoctor-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета asciidoctor.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.adoc LICENSE README-de.adoc README-fr.adoc README-jp.adoc README-zh_CN.adoc README.adoc CONTRIBUTING.adoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n asciidoctor
%doc CHANGELOG.adoc LICENSE README-de.adoc README-fr.adoc README-jp.adoc README-zh_CN.adoc README.adoc CONTRIBUTING.adoc
%_bindir/asciidoctor
%_mandir/asciidoctor.*

%if_enabled    doc
%files         -n gem-asciidoctor-doc
%doc CHANGELOG.adoc LICENSE README-de.adoc README-fr.adoc README-jp.adoc README-zh_CN.adoc README.adoc CONTRIBUTING.adoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-asciidoctor-devel
%doc CHANGELOG.adoc LICENSE README-de.adoc README-fr.adoc README-jp.adoc README-zh_CN.adoc README.adoc CONTRIBUTING.adoc
%endif


%changelog
* Thu Oct 01 2026 Pavel Skrylev <majioa@altlinux.org> 2.0.26-alt1.1
- ! fixed lost deps to ruby binary

* Sun May 31 2026 Pavel Skrylev <majioa@altlinux.org> 2.0.26-alt1
- ^ 2.0.20 -> 2.0.26

* Mon Nov 13 2023 Evgeny Sinelnikov <sin@altlinux.org> 2.0.20-alt1
- ^ 2.0.18 -> 2.0.20

* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 2.0.18-alt1
- ^ 2.0.16 -> 2.0.18

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
