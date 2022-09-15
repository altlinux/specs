%define        gemname idn-ruby

Name:          gem-idn-ruby
Version:       0.1.4
Release:       alt1
Summary:       LibIDN Ruby Bindings
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/deepfryed/idn-ruby
Vcs:           https://github.com/deepfryed/idn-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libidn-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(idn-ruby) = 0.1.4


%description
Ruby Bindings for the GNU LibIDN library, an implementation of the Stringprep,
Punycode and IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group. Included are the most important parts of the
Stringprep, Punycode and IDNA APIs like performing Stringprep processings,
encoding to and decoding from Punycode strings and converting entire domain
names to and from the ACE encoded form.


%package       -n gem-idn-ruby-devel
Version:       0.1.4
Release:       alt1
Summary:       LibIDN Ruby Bindings development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета idn-ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(idn-ruby) = 0.1.4
Requires:      libidn-devel

%description   -n gem-idn-ruby-devel
LibIDN Ruby Bindings development package.

Ruby Bindings for the GNU LibIDN library, an implementation of the Stringprep,
Punycode and IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group. Included are the most important parts of the
Stringprep, Punycode and IDNA APIs like performing Stringprep processings,
encoding to and decoding from Punycode strings and converting entire domain
names to and from the ACE encoded form.

%description   -n gem-idn-ruby-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета idn-ruby.


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
%ruby_gemextdir

%files         -n gem-idn-ruby-devel
%doc README.md
%ruby_includedir/idn*


%changelog
* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.4-alt1
- ^ 0.1.0 -> 0.1.4

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt2.1
- ! spec tags

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt2
- ! spec according to changelog rules

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt1
- + packaged gem with usage Ruby Policy 2.0
