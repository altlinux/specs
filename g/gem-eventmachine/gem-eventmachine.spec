%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname eventmachine

Name:          gem-eventmachine
Version:       1.3.1.4
Release:       alt0.1
Summary:       Fast, simple event-processing library for Ruby programs
License:       Ruby or GPL-2.0
Group:         Development/Ruby
Url:           http://www.rubyeventmachine.com/
Vcs:           https://github.com/eventmachine/eventmachine.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gcc-c++
BuildRequires: net-tools
BuildRequires: /proc
BuildRequires: libssl-devel
%if_enabled check
BuildRequires: gem(test-unit) >= 3.2
BuildRequires: gem(rake-compiler) >= 1.1
BuildRequires: gem(rake-compiler-dock) >= 0.6.3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(net-smtp) >= 0
BuildRequires: gem(yard) >= 0.8.5.2
BuildRequires: gem(redcarpet) >= 0
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rake-compiler-dock) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake-compiler-dock >= 1.2.1,rake-compiler-dock < 2
Obsoletes:     ruby-eventmachine < %EVR
Provides:      ruby-eventmachine = %EVR
Provides:      gem(eventmachine) = 1.3.1.4

%ruby_use_gem_version eventmachine:1.3.1.4

%description
EventMachine implements a fast, single-threaded engine for arbitrary network
communications. It's extremely easy to use in Ruby. EventMachine wraps all
interactions with IP sockets, allowing programs to concentrate on the
implementation of network protocols. It can be used to create both network
servers and clients. To create a server or client, a Ruby program only needs to
specify the IP address and port, and provide a Module that implements the
communications protocol. Implementations of several standard network protocols
are provided with the package, primarily to serve as examples. The real goal of
EventMachine is to enable programs to easily interface with other programs using
TCP/IP, especially if custom protocols are required.


%if_enabled    doc
%package       -n gem-eventmachine-doc
Version:       1.3.1.4
Release:       alt0.1
Summary:       Fast, simple event-processing library for Ruby programs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета eventmachine
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(eventmachine) = 1.3.1.4

%description   -n gem-eventmachine-doc
Fast, simple event-processing library for Ruby programs documentation
files.

EventMachine implements a fast, single-threaded engine for arbitrary network
communications. It's extremely easy to use in Ruby. EventMachine wraps all
interactions with IP sockets, allowing programs to concentrate on the
implementation of network protocols. It can be used to create both network
servers and clients. To create a server or client, a Ruby program only needs to
specify the IP address and port, and provide a Module that implements the
communications protocol. Implementations of several standard network protocols
are provided with the package, primarily to serve as examples. The real goal of
EventMachine is to enable programs to easily interface with other programs using
TCP/IP, especially if custom protocols are required.

%description   -n gem-eventmachine-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета eventmachine.
%endif


%if_enabled    devel
%package       -n gem-eventmachine-devel
Version:       1.3.1.4
Release:       alt0.1
Summary:       Fast, simple event-processing library for Ruby programs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета eventmachine
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(eventmachine) = 1.3.1.4
Requires:      gem(test-unit) >= 3.2
Requires:      gem(rake-compiler) >= 1.1
Requires:      gem(rake-compiler-dock) >= 0.6.3
Requires:      gem(rake) >= 0
Requires:      gem(net-smtp) >= 0
Requires:      gem(yard) >= 0.8.5.2
Requires:      gem(redcarpet) >= 0
Requires:      gcc-c++
Requires:      net-tools
Requires:      /proc
Requires:      libssl-devel
Conflicts:     gem(test-unit) >= 4
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rake-compiler-dock) >= 2

%description   -n gem-eventmachine-devel
Fast, simple event-processing library for Ruby programs development
package.

EventMachine implements a fast, single-threaded engine for arbitrary network
communications. It's extremely easy to use in Ruby. EventMachine wraps all
interactions with IP sockets, allowing programs to concentrate on the
implementation of network protocols. It can be used to create both network
servers and clients. To create a server or client, a Ruby program only needs to
specify the IP address and port, and provide a Module that implements the
communications protocol. Implementations of several standard network protocols
are provided with the package, primarily to serve as examples. The real goal of
EventMachine is to enable programs to easily interface with other programs using
TCP/IP, especially if custom protocols are required.

%description   -n gem-eventmachine-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета eventmachine.
%endif


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

%if_enabled    doc
%files         -n gem-eventmachine-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-eventmachine-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Wed Jul 31 2024 Pavel Skrylev <majioa@altlinux.org> 1.3.1.4-alt0.1
- ^ 1.3.0.dev.1 -> 1.3.[1p4]

* Fri Oct 08 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.0.dev.1-alt1
- ^ 1.2.7 -> 1.3.0.dev.1

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.7-alt3
- ! spec tags and syntax

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.7-alt2
- > Ruby Policy 2.0

* Mon Sep 03 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1.2
- Rebuild with new Ruby autorequirements.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.2.7-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Sun May 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1
- New version.

* Tue May 01 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.6-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1.1
- Rebuild with Ruby 2.4.1

* Mon Jul 31 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1
- New version

* Tue Mar 14 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.3-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.0.1-alt3
- Rebuild with new %%ruby_sitearchdir location

* Sat Sep 10 2016 Andrey Cherepanov <cas@altlinux.org> 1.2.0.1-alt2
- Rebuild with Ruby 2.3.1

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.2.0.1-alt1
- New version

* Mon Apr 21 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- New version
- Restore package in Sisyphus
- Disable all tests

* Wed Nov 17 2010 Timur Batyrshin <erthad@altlinux.org> 0.12.11-alt3
- rebuild with new openssl

* Thu Jul 01 2010 Timur Batyrshin <erthad@altlinux.org> 0.12.11-alt2
- fixed tests

* Mon Jun 28 2010 Timur Batyrshin <erthad@altlinux.org> 0.12.11-alt1
- Built for Sisyphus
