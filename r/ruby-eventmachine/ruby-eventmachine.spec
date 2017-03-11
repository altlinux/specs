# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname eventmachine

#	disable if you do not have direct connection to internet
%def_without Internet
#	enable if you build the package on OpenVZ kernel
%def_without OpenVZ

Name:    ruby-%pkgname
Version: 1.2.3
Release: alt1

Summary: Fast, simple event-processing library for Ruby programs
Group:   Development/Ruby
License: MIT/Ruby
Url:     http://www.rubyeventmachine.com/ 

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: libruby-devel ruby-tool-setup ruby-tool-rdoc
BuildRequires: gcc-c++ libssl-devel net-tools /proc

%filter_from_requires \,^ruby(\(java\|jeventmachine\|win32/resolv\|em/spec\)),d

%description
EventMachine implements a fast, single-threaded engine for arbitrary network
communications. It's extremely easy to use in Ruby. EventMachine wraps all
interactions with IP sockets, allowing programs to concentrate on the
implementation of network protocols. It can be used to create both network
servers and clients. To create a server or client, a Ruby program only needs
to specify the IP address and port, and provide a Module that implements the
communications protocol. Implementations of several standard network protocols
are provided with the package, primarily to serve as examples. The real goal
of EventMachine is to enable programs to easily interface with other programs
using TCP/IP, especially if custom protocols are required.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
rm -f lib/jeventmachine.rb lib/em/protocols/postgres3.rb
sed -i 's,\(.*postgres.*\),#&,' lib/em/protocols.rb
%ruby_config
%ruby_build

%check
%if_without Internet
export SKIPTESTS="-x test_get_sock_opt.rb -x test_httpclient.rb -x test_httpclient2.rb"
%endif

%if_with OpenVZ
export SKIPTESTS="$SKIPTESTS -x test_file_watch.rb"
%endif

# TODO %%ruby_test_unit -Ilib:ext:test $SKIPTESTS tests

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%files
%doc README.md docs examples
%ruby_sitearchdir/*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/BufferedTokenizer*
%ruby_ri_sitedir/EM/*
%ruby_ri_sitedir/EventMachine*
%ruby_ri_sitedir/IO/*
%ruby_ri_sitedir/TestConnection/*

%changelog
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

