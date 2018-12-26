%define _unpackaged_files_terminate_build 1

Name: ruby-makeconf
Version: 0.3.0
Release: alt2.svn20130509
Summary: Build system for C programs
License: MIT
Group: Development/Ruby
Url: https://sourceforge.net/projects/makeconf/

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
Makeconf is a build system for C programs. It was inspired by GNU
Autoconf, and tries to be backwards compatible from an end-user
perspective. Makeconf allows you to specify information that you need to
build software, and then it generates a configure script for you. This
script takes care of generating a makefile that can build your software
package.

%package doc
Summary: Documentation for Makeconf
Group: Development/Documentation
BuildArch: noarch

%description doc
Makeconf is a build system for C programs. It was inspired by GNU
Autoconf, and tries to be backwards compatible from an end-user
perspective. Makeconf allows you to specify information that you need to
build software, and then it generates a configure script for you. This
script takes care of generating a makefile that can build your software
package.

This package contains documentation for Makeconf.

%prep
%setup
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%files
%doc BUGS README TODO
%_bindir/*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Dec 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt2.svn20130509
- Fixed build.

* Wed Feb 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.svn20130509
- Initial build for Sisyphus

