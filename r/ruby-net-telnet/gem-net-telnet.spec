%define  pkgname net-telnet

Name:    ruby-%pkgname
Version: 0.2.0
Release: alt1

Summary: Provides telnet client functionality.
License: BSD 2-clause Simplified License
Group:   Development/Ruby
Url:     https://github.com/ruby/net-telnet.git

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
Provides telnet client functionality.

This class also has, through delegation, all the methods of a socket object
(by default, a TCPSocket, but can be set by the Proxy option to new()). This
provides methods such as close() to end the session and sysread() to read data
directly from the host, instead of via the waitfor() mechanism. Note that if you
do use sysread() directly when in telnet mode, you should probably pass the
output through preprocess() to extract telnet command sequences.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build
rm -f bin/{console,setup}

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
#%rake_test

%files
%doc *.md
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Jan 14 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus, packaged as a gem
