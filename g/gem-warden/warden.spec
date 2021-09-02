%define        gemname warden

Name:          gem-warden
Version:       1.2.9
Release:       alt1
Summary:       General Rack Authentication Framework
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/wardencommunity/warden
Vcs:           https://github.com/wardencommunity/warden.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rack) >= 2.0.9 gem(rack) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rack) >= 2.0.9 gem(rack) < 3
Obsoletes:     ruby-warden < %EVR
Provides:      ruby-warden = %EVR
Provides:      gem(warden) = 1.2.9


%description
Warden is rack based middleware, designed to provide a mechanism for
authentication in Ruby web applications. It is a common mechanism that fits into
the Rack Machinery to offer powerful options for authentication.


%package       -n gem-warden-doc
Version:       1.2.9
Release:       alt1
Summary:       General Rack Authentication Framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета warden
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(warden) = 1.2.9

%description   -n gem-warden-doc
General Rack Authentication Framework documentation files.

Warden is rack based middleware, designed to provide a mechanism for
authentication in Ruby web applications. It is a common mechanism that fits into
the Rack Machinery to offer powerful options for authentication.

%description   -n gem-warden-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета warden.


%package       -n gem-warden-devel
Version:       1.2.9
Release:       alt1
Summary:       General Rack Authentication Framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета warden
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(warden) = 1.2.9

%description   -n gem-warden-devel
General Rack Authentication Framework development package.

Warden is rack based middleware, designed to provide a mechanism for
authentication in Ruby web applications. It is a common mechanism that fits into
the Rack Machinery to offer powerful options for authentication.

%description   -n gem-warden-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета warden.


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

%files         -n gem-warden-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-warden-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.9-alt1
- ^ 1.2.8 -> 1.2.9

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.8-alt1
- Bump to 1.2.8
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt2.2
- Rebuild with new Ruby autorequirements.

* Tue Dec 04 2012 Led <led@altlinux.ru> 0.9.4-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Mar 02 2010 Timur Batyrshin <erthad@altlinux.org> 0.9.4-alt2
- added README.alt

* Wed Feb 24 2010 Timur Batyrshin <erthad@altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus
