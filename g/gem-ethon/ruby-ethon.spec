%define        gemname ethon

Name:          gem-ethon
Version:       0.14.0
Release:       alt1
Summary:       Very simple libcurl wrapper
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/typhoeus/ethon
Vcs:           https://github.com/typhoeus/ethon.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libruby-devel
BuildRequires: gem(ffi) >= 1.15.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ffi) >= 1.15.0
Obsoletes:     ruby-ethon < %EVR
Provides:      ruby-ethon = %EVR
Provides:      gem(ethon) = 0.14.0


%description
In Greek mythology, Ethon, the son of Typhoeus and Echidna, is a gigantic eagle.
So much for the history. In the modern world, Ethon is a very basic libcurl
wrapper using ffi.


%package       -n gem-ethon-doc
Version:       0.14.0
Release:       alt1
Summary:       Very simple libcurl wrapper documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ethon
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ethon) = 0.14.0

%description   -n gem-ethon-doc
Very simple libcurl wrapper documentation files.

In Greek mythology, Ethon, the son of Typhoeus and Echidna, is a gigantic eagle.
So much for the history. In the modern world, Ethon is a very basic libcurl
wrapper using ffi.

%description   -n gem-ethon-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ethon.


%package       -n gem-ethon-devel
Version:       0.14.0
Release:       alt1
Summary:       Very simple libcurl wrapper development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ethon
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ethon) = 0.14.0

%description   -n gem-ethon-devel
Very simple libcurl wrapper development package.

In Greek mythology, Ethon, the son of Typhoeus and Echidna, is a gigantic eagle.
So much for the history. In the modern world, Ethon is a very basic libcurl
wrapper using ffi.

%description   -n gem-ethon-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ethon.


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

%files         -n gem-ethon-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ethon-devel
%doc README.md


%changelog
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.14.0-alt1
- ^ 0.9.1 -> 0.14.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.1-alt1.2
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.1-alt1.1
- Rebuild with Ruby 2.4.1

* Wed Mar 29 2017 Denis Medvedev <nbr@altlinux.org> 0.9.1-alt1
- Initial sisyphus release
