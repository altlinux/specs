%define pkgname facter

Name: 	 ruby-%pkgname
Version: 2.0.1
Release: alt2

Summary: Ruby library for retrieving facts from operating systems
Group:   Development/Ruby
License: Apache-2.0
Url: 	 https://tickets.puppetlabs.com/browse/FACT
# VCS:	 https://github.com/puppetlabs/facter

BuildArch: noarch

Source:  %pkgname-%version.tar
Patch1:  %name-alt-support.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

Requires: coreutils dmidecode net-tools pciutils bind-utils

%filter_from_requires /^ruby(.*\(win32\|windows\/\|cfpropertylist\|sys\/admin\|augeas\|puppet\).*/d

%description
A cross-platform Ruby library for retrieving facts from
operating systems. Supports multiple resolution mechanisms, any
of which can be restricted to working only on certain operating
systems or environments. Facter is especially useful for
retrieving things like operating system names, IP addresses, MAC
addresses, and SSH keys.

It is easy to extend Facter to include your own custom facts or
to include additional mechanisms for retrieving facts.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%patch1 -p1
# Remove unmets
#rm -f lib/facter/util/windows_root.rb \
#      lib/facter/util/macosx.rb

%update_setup_rb

%build
%ruby_config
%ruby_build

%install
#./install.rb --destdir=%buildroot
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc *.md
%_bindir/%pkgname
%ruby_sitelibdir/*
%doc %_man8dir/%{pkgname}.*

%files doc
%ruby_ri_sitedir/*
 
%changelog
* Wed Jan 18 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt2
- Add ALT Linux operating system support
- Add bind-utils for IP address get

* Mon Apr 28 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version

* Fri Nov 30 2012 Led <led@altlinux.ru> 1.6.8-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Apr 27 2012 Sergey Alembekov <rt@altlinux.ru> 1.6.8-alt1
- [1.6.8]

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.5.6-alt1
- [1.5.6]

* Fri Oct 31 2008 Sir Raorn <raorn@altlinux.ru> 1.5.2-alt1
- [1.5.2]

* Wed Sep 03 2008 Sir Raorn <raorn@altlinux.ru> 1.5.1-alt1
- Built for Sisyphus

