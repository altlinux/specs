%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname Ascii85

Name:          gem-ascii85
Version:       1.1.1
Release:       alt1
Summary:       Ascii85 encoder/decoder
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/DataWraith/ascii85gem/
Vcs:           https://github.com/datawraith/ascii85gem.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         fix-binary.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.0.0
BuildRequires: gem(minitest) >= 2.6.0
BuildRequires: gem(rake) >= 0.9.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names Ascii85,ascii85
Provides:      gem(Ascii85) = 1.1.1


%description
Ascii85 provides methods to encode/decode Adobe's binary-to-text encoding of the
same name.


%package       -n ascii85
Version:       1.1.1
Release:       alt1
Summary:       Ascii85 encoder/decoder executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета Ascii85
Group:         Other
BuildArch:     noarch

Requires:      gem(Ascii85) = 1.1.1

%description   -n ascii85
Ascii85 encoder/decoder executable(s).

Ascii85 provides methods to encode/decode Adobe's binary-to-text encoding of the
same name.

%description   -n ascii85 -l ru_RU.UTF-8
Исполнямка для самоцвета Ascii85.


%if_enabled    doc
%package       -n gem-ascii85-doc
Version:       1.1.1
Release:       alt1
Summary:       Ascii85 encoder/decoder documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета Ascii85
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(Ascii85) = 1.1.1

%description   -n gem-ascii85-doc
Ascii85 encoder/decoder documentation files.

Ascii85 provides methods to encode/decode Adobe's binary-to-text encoding of the
same name.

%description   -n gem-ascii85-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета Ascii85.
%endif


%if_enabled    devel
%package       -n gem-ascii85-devel
Version:       1.1.1
Release:       alt1
Summary:       Ascii85 encoder/decoder development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета Ascii85
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(Ascii85) = 1.1.1
Requires:      gem(bundler) >= 1.0.0
Requires:      gem(minitest) >= 2.6.0
Requires:      gem(rake) >= 0.9.2

%description   -n gem-ascii85-devel
Ascii85 encoder/decoder development package.

Ascii85 provides methods to encode/decode Adobe's binary-to-text encoding of the
same name.

%description   -n gem-ascii85-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета Ascii85.
%endif


%prep
%setup
%autopatch

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

%files         -n ascii85
%doc README.md
%_bindir/ascii85

%if_enabled    doc
%files         -n gem-ascii85-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ascii85-devel
%doc README.md
%endif


%changelog
* Wed May 15 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- ^ 1.1.0 -> 1.1.1
- ! fixed binary to run into system folder (closes #50360)

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
