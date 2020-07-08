%define        pkgname net-scp

Name:          gem-%pkgname
Version:       3.0.0
Release:       alt1
Summary:       A pure Ruby implementation of the SCP client protocol
Group:         Development/Ruby
License:       MIT
Url:           https://github.com/net-ssh/net-scp
Vcs:           https://github.com/net-ssh/net-scp.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(net-ssh)
BuildRequires: gem(test-unit)
BuildRequires: gem(mocha)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
Net::SCP is a pure-Ruby implementation of the SCP protocol. This operates over
SSH (and requires the Net::SSH library), and allows files and directory trees
to copied to and from a remote server.


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
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ 2.0.0 -> 3.0.0
- ! spec

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- updated (^) 1.2.1 -> 2.0.0

* Thu Mar 07 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt2
- used (>) Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- New version.
- Disable tests.

* Sat Dec 08 2012 Led <led@altlinux.ru> 1.0.2-alt2.1
- Rebuilt with ruby-1.9.3-alt1
- fixed BuildRequires

* Sat Dec 12 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.2-alt2
- Fixed file conflict in doc subpackage with net-ssh and net-sftp docs
- Enabled tests

* Sat Dec 05 2009 Igor Zubkov <icesik@altlinux.org> 1.0.2-alt1
- build for Sisyphus

