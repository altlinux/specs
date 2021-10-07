%define        gemname ttfunk

Name:          gem-ttfunk
Version:       1.7.0
Release:       alt1
Summary:       TrueType Font Metrics Parser
License:       Nonstandard or GPL-2.0 or GPL-3.0
Group:         Development/Ruby
Url:           https://prawnpdf.org
Vcs:           https://github.com/prawnpdf/ttfunk.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
# BuildRequires: gem(prawn-dev) >= 0.1.0 gem(prawn-dev) < 0.2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(ttfunk) = 1.7.0


%description
Font Metrics Parser for the Prawn PDF generator.


%package       -n gem-ttfunk-doc
Version:       1.7.0
Release:       alt1
Summary:       TrueType Font Metrics Parser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ttfunk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ttfunk) = 1.7.0

%description   -n gem-ttfunk-doc
TrueType Font Metrics Parser documentation files.

Font Metrics Parser for the Prawn PDF generator.

%description   -n gem-ttfunk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ttfunk.


%package       -n gem-ttfunk-devel
Version:       1.7.0
Release:       alt1
Summary:       TrueType Font Metrics Parser development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ttfunk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ttfunk) = 1.7.0
# Requires:      gem(prawn-dev) >= 0.1.0 gem(prawn-dev) < 0.2

%description   -n gem-ttfunk-devel
TrueType Font Metrics Parser development package.

Font Metrics Parser for the Prawn PDF generator.

%description   -n gem-ttfunk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ttfunk.


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

%files         -n gem-ttfunk-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ttfunk-devel
%doc README.md


%changelog
* Sun Sep 12 2021 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- + packaged gem with Ruby Policy 2.0
