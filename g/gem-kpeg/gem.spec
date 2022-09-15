%define        gemname kpeg

Name:          gem-kpeg
Version:       1.3.1
Release:       alt1
Summary:       KPeg is a simple PEG library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/evanphx/kpeg
Vcs:           https://github.com/evanphx/kpeg.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.2 gem(minitest) < 6
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.7 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Provides:      gem(kpeg) = 1.3.1


%description
KPeg is a simple PEG library for Ruby. It provides an API as well as native
grammar to build the grammar.

KPeg strives to provide a simple, powerful API without being too exotic.

KPeg supports direct left recursion of rules via the {OMeta
memoization}[http://www.vpri.org/pdf/tr2008003_experimenting.pdf] trick.


%package       -n kpeg
Version:       1.3.1
Release:       alt1
Summary:       KPeg is a simple PEG library for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета kpeg
Group:         Other
BuildArch:     noarch

Requires:      gem(kpeg) = 1.3.1

%description   -n kpeg
KPeg is a simple PEG library for Ruby executable(s).

KPeg is a simple PEG library for Ruby. It provides an API as well as native
grammar to build the grammar.

KPeg strives to provide a simple, powerful API without being too exotic.

KPeg supports direct left recursion of rules via the {OMeta
memoization}[http://www.vpri.org/pdf/tr2008003_experimenting.pdf] trick.

%description   -n kpeg -l ru_RU.UTF-8
Исполнямка для самоцвета kpeg.


%package       -n gem-kpeg-doc
Version:       1.3.1
Release:       alt1
Summary:       KPeg is a simple PEG library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета kpeg
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(kpeg) = 1.3.1

%description   -n gem-kpeg-doc
KPeg is a simple PEG library for Ruby documentation files.

KPeg is a simple PEG library for Ruby. It provides an API as well as native
grammar to build the grammar.

KPeg strives to provide a simple, powerful API without being too exotic.

KPeg supports direct left recursion of rules via the {OMeta
memoization}[http://www.vpri.org/pdf/tr2008003_experimenting.pdf] trick.

%description   -n gem-kpeg-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета kpeg.


%package       -n gem-kpeg-devel
Version:       1.3.1
Release:       alt1
Summary:       KPeg is a simple PEG library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета kpeg
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(kpeg) = 1.3.1
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 0

%description   -n gem-kpeg-devel
KPeg is a simple PEG library for Ruby development package.

KPeg is a simple PEG library for Ruby. It provides an API as well as native
grammar to build the grammar.

KPeg strives to provide a simple, powerful API without being too exotic.

KPeg supports direct left recursion of rules via the {OMeta
memoization}[http://www.vpri.org/pdf/tr2008003_experimenting.pdf] trick.

%description   -n gem-kpeg-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета kpeg.


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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n kpeg
%doc README.rdoc
%_bindir/kpeg

%files         -n gem-kpeg-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-kpeg-devel
%doc README.rdoc


%changelog
* Tue Aug 23 2022 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- + packaged gem with Ruby Policy 2.0
