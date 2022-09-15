%define        gemname rqrcode

Name:          gem-rqrcode
Version:       2.1.0
Release:       alt1
Summary:       A library to encode QR Codes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/whomwah/rqrcode
Vcs:           https://github.com/whomwah/rqrcode.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rqrcode_core) >= 1.0 gem(rqrcode_core) < 2
BuildRequires: gem(chunky_png) >= 1.0 gem(chunky_png) < 2
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.5 gem(rspec) < 4
BuildRequires: gem(standardrb) >= 1.0 gem(standardrb) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rqrcode_core) >= 1.0 gem(rqrcode_core) < 2
Requires:      gem(chunky_png) >= 1.0 gem(chunky_png) < 2
Obsoletes:     ruby-rqrcode < %EVR
Provides:      ruby-rqrcode = %EVR
Provides:      gem(rqrcode) = 2.1.0


%description
rqrcode is a library for encoding QR Codes. The simple interface allows you to
create QR Code data structures and then render them in the way you choose.


%package       -n gem-rqrcode-doc
Version:       2.1.0
Release:       alt1
Summary:       A library to encode QR Codes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rqrcode
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rqrcode) = 2.1.0

%description   -n gem-rqrcode-doc
A library to encode QR Codes documentation files.

rqrcode is a library for encoding QR Codes. The simple interface allows you to
create QR Code data structures and then render them in the way you choose.

%description   -n gem-rqrcode-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rqrcode.


%package       -n gem-rqrcode-devel
Version:       2.1.0
Release:       alt1
Summary:       A library to encode QR Codes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rqrcode
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rqrcode) = 2.1.0
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.5 gem(rspec) < 4
Requires:      gem(standardrb) >= 1.0 gem(standardrb) < 2

%description   -n gem-rqrcode-devel
A library to encode QR Codes development package.

rqrcode is a library for encoding QR Codes. The simple interface allows you to
create QR Code data structures and then render them in the way you choose.

%description   -n gem-rqrcode-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rqrcode.


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

%files         -n gem-rqrcode-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rqrcode-devel
%doc README.md


%changelog
* Thu Jun 30 2022 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 1.1.2 -> 2.1.0

* Mon Feb 03 2020 Alexey Shabalin <shaba@altlinux.org> 1.1.2-alt1
- Initial build.
