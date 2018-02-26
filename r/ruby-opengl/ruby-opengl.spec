Name: ruby-opengl
Version: 0.60.1
Release: alt2
Summary: OpenGL Interface for Ruby
License: MIT
Group: Development/Ruby
Url: http://ruby-opengl.rubyforge.org/
Source: ruby-opengl-%{version}.tar
Patch: ruby-opengl-0.60.1-alt-rubygems-sucks.patch
Patch1: ruby-opengl-alt-STR2CSTR.patch

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

# Automatically added by buildreq on Thu Apr 03 2008 (-bi)
BuildRequires: libGL-devel libX11-devel libfreeglut-devel libruby-devel ruby-mkrf

%description
ruby-opengl consists of Ruby extension modules that are bindings for 
the OpenGL, GLU, and GLUT libraries. It is intended to be a replacement
for -- and uses the code from -- Yoshi's ruby-opengl.

%prep
%setup
%patch -p1
%patch1 -p2

%build
%rake
#rake test

%install
mkdir -p %buildroot{%ruby_sitelibdir,%ruby_sitearchdir}
install -p -m644 lib/*.so  %buildroot%ruby_sitearchdir
install -p -m644 lib/*.rb  %buildroot%ruby_sitelibdir

%files
%ruby_sitelibdir/*
%ruby_sitearchdir/*
%doc doc

%changelog
* Sun Sep 26 2010 Alexey I. Froloff <raorn@altlinux.org> 0.60.1-alt2
- Rebuild with Ruby 1.9.2

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.60.1-alt1
- [0.60.1]

* Thu Apr 03 2008 Sir Raorn <raorn@altlinux.ru> 0.60-alt1
- Rebuilt with rpm-build-ruby
- Based on unpublished build:
  * Mon Mar 24 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.60-alt1
  - 0.60
  - new upstream maintainer(see http://ruby-opengl.rubyforge.org/)
  - MIT licence

* Sat May 08 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.32d-alt4
- New version
- Use default gcc for building

* Fri Feb 13 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.32b-alt3
- BuildRequires fixed

* Thu Feb 05 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.32b-alt2
- Use set_gcc_version to select gcc

* Sat Jan 10 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.32b-alt1
- First Build for ALT project
