%define        pkgname em-socksify

Name: 	       gem-%pkgname
Version:       0.3.2.1
Release:       alt1
Summary:       EventMachine SOCKSify shim: adds SOCKS support to any protocol
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/igrigorik/em-socksify
Vcs:           https://github.com/igrigorik/em-socksify.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(eventmachine)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
Dealing with SOCKS and HTTP proxies is a pain. EM-Socksify provides a
simple ship to setup and negotiation a SOCKS / HTTP connection for any
EventMachine protocol.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --use=%gemname --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Mon Apr 13 2020 Pavel Skrylev <majioa@altlinux.org> 0.3.2.1-alt1
- > Ruby Policy 2.0
- ^ 0.3.2 -> 0.3.2.1pre
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
