%define        gemname em-socksify

Name:          gem-em-socksify
Version:       0.3.2.1
Release:       alt1.1
Summary:       EventMachine SOCKSify shim: adds SOCKS support to any protocol
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/igrigorik/em-socksify
Vcs:           https://github.com/igrigorik/em-socksify.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(eventmachine) >= 1.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(eventmachine) >= 1.0.0
Obsoletes:     ruby-em-socksify < %EVR
Provides:      ruby-em-socksify = %EVR
Provides:      gem(em-socksify) = 0.3.2.1

%ruby_use_gem_version em-socksify:0.3.2.1

%description
Dealing with SOCKS and HTTP proxies is a pain. EM-Socksify provides a simple
ship to setup and negotiation a SOCKS / HTTP connection for any EventMachine
protocol.


%package       -n gem-em-socksify-doc
Version:       0.3.2.1
Release:       alt1.1
Summary:       EventMachine SOCKSify shim: adds SOCKS support to any protocol documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета em-socksify
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(em-socksify) = 0.3.2.1

%description   -n gem-em-socksify-doc
EventMachine SOCKSify shim: adds SOCKS support to any protocol documentation
files.

%description   -n gem-em-socksify-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета em-socksify.


%package       -n gem-em-socksify-devel
Version:       0.3.2.1
Release:       alt1.1
Summary:       EventMachine SOCKSify shim: adds SOCKS support to any protocol development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета em-socksify
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(em-socksify) = 0.3.2.1
Requires:      gem(rspec) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-em-socksify-devel
EventMachine SOCKSify shim: adds SOCKS support to any protocol development
package.

%description   -n gem-em-socksify-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета em-socksify.


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

%files         -n gem-em-socksify-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-em-socksify-devel
%doc README.md


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 0.3.2.1-alt1.1
- ^ ! spec deps

* Mon Apr 13 2020 Pavel Skrylev <majioa@altlinux.org> 0.3.2.1-alt1
- > Ruby Policy 2.0
- ^ 0.3.2 -> 0.3.2[1]
- ! spec tags and syntax

* Sun Aug 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt2.1
- Rebuild for new Ruby autorequirements.

* Wed Jul 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt2
- Build from upstream tag.
- Use correct sources.
- Package as gem.

* Thu Jan 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1
- New version.

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 0.3.1-alt1
- New version

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Initial build for ALT Linux
