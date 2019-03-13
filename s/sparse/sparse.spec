Name:		sparse
Version:	0.6.1
Release:	alt1_rc1
Summary: 	A semantic parser for C
License:	MIT
Group:		Development/Kernel
#Git:		https://git.kernel.org/pub/scm/devel/sparse/sparse.git
Url:		http://sparse.wiki.kernel.org/
Source:		%name-%version.tar
BuildRequires:	libxml2-devel
# for test-inspect:
BuildRequires:	libgtk+3-devel

%description
Sparse, the semantic parser, provides a compiler frontend capable of parsing
most of ANSI C as well as many GCC extensions, and a collection of sample
compiler backends, including a static analyzer also called "sparse". Sparse
provides a set of annotations designed to convey semantic information about
types, such as what address space pointers point to, or what locks a function
acquires or releases.

Sparse is primarily used in the development and debugging of the Linux kernel.

%prep
%setup -q

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%check
%make_build check

%files
%doc LICENSE README FAQ
%{_bindir}/sparse
%{_bindir}/cgcc
%{_bindir}/c2xml
%{_bindir}/test-inspect
%{_mandir}/man1/*

%changelog
* Wed Mar 13 2019 Vitaly Chikunov <vt@altlinux.org> 0.6.1-alt1_rc1
- First import of v0.6.1-rc1-2-g7fd3778.
- Newer version than in autoimports (0.6.0) and uses gtk3.
