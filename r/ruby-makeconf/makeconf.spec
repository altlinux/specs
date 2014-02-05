Name: ruby-makeconf
Version: 0.3.0
Release: alt1.svn20130509
Summary: Build system for C programs
License: MIT
Group: Development/Ruby
Url: https://sourceforge.net/projects/makeconf/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: rpm-build-ruby

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

%build
%make gem
 
%install
gem install makeconf --no-ri -i %buildroot%ruby_sitelibdir
%rdoc lib/

pushd %buildroot%ruby_sitelibdir
mv gems/makeconf-0.3.0/lib/* ./
rm -f makeconf/wxapp.rb
mv gems/makeconf-0.3.0/bin/bootstrap.sh bin/
rm -fR gems
popd

%files
%doc BUGS README TODO
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Feb 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.svn20130509
- Initial build for Sisyphus

