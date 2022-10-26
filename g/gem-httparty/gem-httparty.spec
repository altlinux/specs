%define        gemname httparty

Name:          gem-httparty
Version:       0.20.0
Release:       alt1
Summary:       Makes http fun! Also, makes consuming restful web services dead easy
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jnunemaker/httparty
Vcs:           https://github.com/jnunemaker/httparty.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(mongrel) = 1.2.0.pre2
BuildRequires: gem(guard) >= 0
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(guard-bundler) >= 0
BuildRequires: gem(rspec) >= 3.4 gem(rspec) < 4
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(aruba) >= 0
BuildRequires: gem(cucumber) >= 2.3 gem(cucumber) < 3
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(addressable) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(multi_xml) >= 0.5.2
BuildRequires: gem(mime-types) >= 3.0 gem(mime-types) < 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(multi_xml) >= 0.5.2
Requires:      gem(mime-types) >= 3.0 gem(mime-types) < 4
Provides:      gem(httparty) = 0.20.0


%description
Makes http fun! Also, makes consuming restful web services dead easy.


%package       -n httparty
Version:       0.20.0
Release:       alt1
Summary:       Makes http fun! Also, makes consuming restful web services dead easy executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета httparty
Group:         Other
BuildArch:     noarch

Requires:      gem(httparty) = 0.20.0

%description   -n httparty
Makes http fun! Also, makes consuming restful web services dead easy
executable(s).

%description   -n httparty -l ru_RU.UTF-8
Исполнямка для самоцвета httparty.


%package       -n gem-httparty-doc
Version:       0.20.0
Release:       alt1
Summary:       Makes http fun! Also, makes consuming restful web services dead easy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета httparty
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(httparty) = 0.20.0

%description   -n gem-httparty-doc
Makes http fun! Also, makes consuming restful web services dead easy
documentation files.

%description   -n gem-httparty-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета httparty.


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

%files         -n httparty
%doc README.md
%_bindir/httparty

%files         -n gem-httparty-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.20.0-alt1
- + packaged gem with Ruby Policy 2.0
