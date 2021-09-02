%define        gemname deacon

Name:          gem-deacon
Version:       1.0.0
Release:       alt2.1
Summary:       Human readable name generator plugin
License:       GPLv3 or Public domain
Group:         Development/Ruby
Url:           https://github.com/lzap/deacon
Vcs:           https://github.com/lzap/deacon.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rdoc) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-deacon < %EVR
Provides:      ruby-deacon = %EVR
Provides:      gem(deacon) = 1.0.0


%description
Out of ideas for incoming bare-metal host names in your cluster? This little gem
is a way out! It contains frequently occurring given names and surnames from the
1990 US Census (public domain data):

* 256 (8 bits) unique male given names
* 256 (8 bits) unique female given names
* 65,536 (16 bits) unique surnames

Given names were filtered to be 3-5 characters long, surnames 5-8 characters,
therefore generated names are never longer than 14 characters (5+1+8).

This gives 33,554,432 (25 bits) total of male and female name combinations.
Built-in generator can either generate randomized succession, or generate
combinations based on MAC adresses.


%package       -n gem-deacon-doc
Version:       1.0.0
Release:       alt2.1
Summary:       Human readable name generator plugin documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета deacon
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(deacon) = 1.0.0

%description   -n gem-deacon-doc
Human readable name generator plugin documentation files.

Out of ideas for incoming bare-metal host names in your cluster? This little gem
is a way out! It contains frequently occurring given names and surnames from the
1990 US Census (public domain data):

* 256 (8 bits) unique male given names
* 256 (8 bits) unique female given names
* 65,536 (16 bits) unique surnames

Given names were filtered to be 3-5 characters long, surnames 5-8 characters,
therefore generated names are never longer than 14 characters (5+1+8).

This gives 33,554,432 (25 bits) total of male and female name combinations.
Built-in generator can either generate randomized succession, or generate
combinations based on MAC adresses.

%description   -n gem-deacon-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета deacon.


%package       -n gem-deacon-devel
Version:       1.0.0
Release:       alt2.1
Summary:       Human readable name generator plugin development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета deacon
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(deacon) = 1.0.0
Requires:      gem(rdoc) >= 0 gem(rdoc) < 7

%description   -n gem-deacon-devel
Human readable name generator plugin development package.

Out of ideas for incoming bare-metal host names in your cluster? This little gem
is a way out! It contains frequently occurring given names and surnames from the
1990 US Census (public domain data):

* 256 (8 bits) unique male given names
* 256 (8 bits) unique female given names
* 65,536 (16 bits) unique surnames

Given names were filtered to be 3-5 characters long, surnames 5-8 characters,
therefore generated names are never longer than 14 characters (5+1+8).

This gives 33,554,432 (25 bits) total of male and female name combinations.
Built-in generator can either generate randomized succession, or generate
combinations based on MAC adresses.

%description   -n gem-deacon-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета deacon.


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

%files         -n gem-deacon-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-deacon-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2.1
- ! spec

* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2
- Use Ruby Policy 2.0

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- Initial gemified build for Sisyphus
