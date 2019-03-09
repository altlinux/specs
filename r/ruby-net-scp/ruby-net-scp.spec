%define        pkgname net-scp

Name:          ruby-%pkgname
Version:       1.2.1
Release:       alt2
Summary:       A pure Ruby implementation of the SCP client protocol
Group:         Development/Ruby
License:       MIT
Url:           https://github.com/net-ssh/net-scp
# VCS:         https://github.com/net-ssh/net-scp.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(net-ssh)
BuildRequires: gem(test-unit)
BuildRequires: ruby-mocha

%description
Net::SCP is a pure-Ruby implementation of the SCP protocol. This operates over
SSH (and requires the Net::SSH library), and allows files and directory trees
to copied to and from a remote server.


%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemlibdir
%ruby_gemspec

%files doc
%ruby_gemdocdir

%changelog
* Thu Mar 07 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt2
- Use Ruby Policy 2.0.

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

