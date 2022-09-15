%define        gemname rqrcode_core

Name:          gem-rqrcode-core
Version:       1.2.0
Release:       alt1
Summary:       A library to encode QR Codes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/chuckremes/ffi-rzmq-core.git
Vcs:           https://github.com/chuckremes/ffi-rzmq-core.git.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(standardrb) >= 1.0 gem(standardrb) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-rqrcode_core < %EVR
Provides:      ruby-rqrcode_core = %EVR
Provides:      gem(rqrcode_core) = 1.2.0


%description
rqrcode_core is a Ruby library for encoding QR Codes. The simple interface (with
no runtime dependencies) allows you to create QR Code data structures.


%package       -n gem-rqrcode-core-doc
Version:       1.2.0
Release:       alt1
Summary:       A library to encode QR Codes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rqrcode_core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rqrcode_core) = 1.2.0

%description   -n gem-rqrcode-core-doc
A library to encode QR Codes documentation files.

rqrcode_core is a Ruby library for encoding QR Codes. The simple interface (with
no runtime dependencies) allows you to create QR Code data structures.

%description   -n gem-rqrcode-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rqrcode_core.


%package       -n gem-rqrcode-core-devel
Version:       1.2.0
Release:       alt1
Summary:       A library to encode QR Codes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rqrcode_core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rqrcode_core) = 1.2.0
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(standardrb) >= 1.0 gem(standardrb) < 2

%description   -n gem-rqrcode-core-devel
A library to encode QR Codes development package.

rqrcode_core is a Ruby library for encoding QR Codes. The simple interface (with
no runtime dependencies) allows you to create QR Code data structures.

%description   -n gem-rqrcode-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rqrcode_core.


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

%files         -n gem-rqrcode-core-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rqrcode-core-devel
%doc README.md


%changelog
* Thu Jun 30 2022 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- ^ 0.1.1 -> 1.2.0

* Mon Feb 03 2020 Alexey Shabalin <shaba@altlinux.org> 0.1.1-alt1
- Initial build.
