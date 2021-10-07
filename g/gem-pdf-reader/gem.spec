%define        gemname pdf-reader

Name:          gem-pdf-reader
Version:       2.5.0
Release:       alt1
Summary:       A library for accessing the content of PDF files
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/yob/pdf-reader
Vcs:           https://github.com/yob/pdf-reader/tree/v2.5.0.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 13.0.1 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.5 gem(rspec) < 4
BuildRequires: gem(cane) >= 3.0 gem(cane) < 4
BuildRequires: gem(morecane) >= 0.2 gem(morecane) < 1
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(Ascii85) >= 1.0 gem(Ascii85) < 2
BuildRequires: gem(ruby-rc4) >= 0
BuildRequires: gem(hashery) >= 2.0 gem(hashery) < 3
BuildRequires: gem(ttfunk) >= 0
BuildRequires: gem(afm) >= 0.2.1 gem(afm) < 0.3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(Ascii85) >= 1.0 gem(Ascii85) < 2
Requires:      gem(ruby-rc4) >= 0
Requires:      gem(hashery) >= 2.0 gem(hashery) < 3
Requires:      gem(ttfunk) >= 0
Requires:      gem(afm) >= 0.2.1 gem(afm) < 0.3
Provides:      gem(pdf-reader) = 2.5.0


%description
The PDF::Reader library implements a PDF parser conforming as much as possible
to the PDF specification from Adobe


%package       -n pdf-utils
Version:       2.5.0
Release:       alt1
Summary:       A library for accessing the content of PDF files executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета pdf-reader
Group:         Other
BuildArch:     noarch

Requires:      gem(pdf-reader) = 2.5.0

%description   -n pdf-utils
A library for accessing the content of PDF files executable(s).

The PDF::Reader library implements a PDF parser conforming as much as possible
to the PDF specification from Adobe

%description   -n pdf-utils -l ru_RU.UTF-8
Исполнямка для самоцвета pdf-reader.


%package       -n gem-pdf-reader-doc
Version:       2.5.0
Release:       alt1
Summary:       A library for accessing the content of PDF files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pdf-reader
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pdf-reader) = 2.5.0

%description   -n gem-pdf-reader-doc
A library for accessing the content of PDF files documentation files.

The PDF::Reader library implements a PDF parser conforming as much as possible
to the PDF specification from Adobe

%description   -n gem-pdf-reader-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pdf-reader.


%package       -n gem-pdf-reader-devel
Version:       2.5.0
Release:       alt1
Summary:       A library for accessing the content of PDF files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pdf-reader
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pdf-reader) = 2.5.0
Requires:      gem(rake) >= 13.0.1 gem(rake) < 14
Requires:      gem(rspec) >= 3.5 gem(rspec) < 4
Requires:      gem(cane) >= 3.0 gem(cane) < 4
Requires:      gem(morecane) >= 0.2 gem(morecane) < 1
Requires:      gem(pry) >= 0
Requires:      gem(rdoc) >= 0

%description   -n gem-pdf-reader-devel
A library for accessing the content of PDF files development package.

The PDF::Reader library implements a PDF parser conforming as much as possible
to the PDF specification from Adobe

%description   -n gem-pdf-reader-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pdf-reader.


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

%files         -n pdf-utils
%doc README.md
%_bindir/pdf_object
%_bindir/pdf_text
%_bindir/pdf_callbacks

%files         -n gem-pdf-reader-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-pdf-reader-devel
%doc README.md


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- + packaged gem with Ruby Policy 2.0
