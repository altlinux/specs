%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname pdf-reader

Name:          gem-pdf-reader
Version:       2.16.0
Release:       alt1
Summary:       A library for accessing the content of PDF files
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/yob/pdf-reader
Vcs:           https://github.com/yob/pdf-reader.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(Ascii85) >= 2.0.0
BuildRequires: gem(afm) >= 0.2.1
BuildRequires: gem(cane) >= 3.0
BuildRequires: gem(hashery) >= 2.0
BuildRequires: gem(morecane) >= 0.2
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rbs-inline) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rspec) >= 3.5
BuildRequires: gem(sorbet) = 0.6.12872
BuildRequires: gem(spoom) >= 0
BuildRequires: gem(tapioca) = 0.17.10
BuildRequires: gem(ttfunk) >= 0
BuildRequires: gem(webrick) >= 0
BuildConflicts: gem(afm) >= 2
BuildConflicts: gem(cane) >= 4
BuildConflicts: gem(hashery) >= 3
BuildConflicts: gem(morecane) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Requires:      ruby >= 2.1
Requires:      gem(Ascii85) >= 2.0.0
Requires:      gem(afm) >= 0.2.1
Requires:      gem(hashery) >= 2.0
Requires:      gem(ttfunk) >= 0
Conflicts:     gem(afm) >= 2
Conflicts:     gem(hashery) >= 3
Provides:      gem(pdf-reader) = 2.16.0

%description
The PDF::Reader library implements a PDF parser conforming as much as possible
to the PDF specification from Adobe


%package       -n pdf
Version:       2.16.0
Release:       alt1
Summary:       A library for accessing the content of PDF files executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета pdf-reader
Group:         Other
BuildArch:     noarch

Requires:      gem(pdf-reader) = 2.16.0
Requires:      gem(rbs-inline) >= 0

%description   -n pdf
A library for accessing the content of PDF files executable(s).

The PDF::Reader library implements a PDF parser conforming as much as possible
to the PDF specification from Adobe

%description   -n pdf -l ru_RU.UTF-8
Исполнямка для самоцвета pdf-reader.


%if_enabled    doc
%package       -n gem-pdf-reader-doc
Version:       2.16.0
Release:       alt1
Summary:       A library for accessing the content of PDF files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pdf-reader
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pdf-reader) = 2.16.0

%description   -n gem-pdf-reader-doc
A library for accessing the content of PDF files documentation files.

The PDF::Reader library implements a PDF parser conforming as much as possible
to the PDF specification from Adobe

%description   -n gem-pdf-reader-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pdf-reader.
%endif


%if_enabled    devel
%package       -n gem-pdf-reader-devel
Version:       2.16.0
Release:       alt1
Summary:       A library for accessing the content of PDF files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pdf-reader
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pdf-reader) = 2.16.0
Requires:      gem(Ascii85) >= 2.0.0
Requires:      gem(afm) >= 0.2.1
Requires:      gem(cane) >= 3.0
Requires:      gem(hashery) >= 2.0
Requires:      gem(morecane) >= 0.2
Requires:      gem(pry) >= 0
Requires:      gem(rbs-inline) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(rspec) >= 3.5
Requires:      gem(sorbet) = 0.6.12872
Requires:      gem(spoom) >= 0
Requires:      gem(tapioca) = 0.17.10
Requires:      gem(ttfunk) >= 0
Requires:      gem(webrick) >= 0
Conflicts:     gem(afm) >= 2
Conflicts:     gem(cane) >= 4
Conflicts:     gem(hashery) >= 3
Conflicts:     gem(morecane) >= 1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-pdf-reader-devel
A library for accessing the content of PDF files development package.

The PDF::Reader library implements a PDF parser conforming as much as possible
to the PDF specification from Adobe

%description   -n gem-pdf-reader-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pdf-reader.
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
%doc CHANGELOG MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n pdf
%doc CHANGELOG MIT-LICENSE README.md
%_bindir/pdf_object
%_bindir/pdf_text
%_bindir/pdf_callbacks

%if_enabled    doc
%files         -n gem-pdf-reader-doc
%doc CHANGELOG MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-pdf-reader-devel
%doc CHANGELOG MIT-LICENSE README.md
%endif


%changelog
* Tue Sep 01 2026 Pavel Skrylev <majioa@altlinux.org> 2.16.0-alt1
- ^ 2.12.0 -> 2.16.0

* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 2.12.0-alt1
- ^ 2.5.0 -> 2.12.0

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- + packaged gem with Ruby Policy 2.0
