Name: mcl
Version: 1.008.09.149
Release: alt2

Summary: Markov cluster algorithm for graphs
License: GPLv3
Group: Sciences/Mathematics
Url: http://www.micans.org/mcl

Packager: Kirill Maslinsky <kirill@altlinux.org>
Source0: %name-%version.tar
Patch1: %name-%version-alt-build.patch

%description
The MCL algorithm is short for the Markov Cluster Algorithm, a fast and scalable 
unsupervised cluster algorithm for graphs based on simulation of (stochastic) 
flow in graphs. The algorithm was invented/discovered by Stijn van Dongen at the 
Centre for Mathematics and Computer Science (also known as CWI) in the 
Netherlands. 

%prep 
%setup %name-%version.tar
%patch1 -p1

%build
autoreconf -fisv
%configure
%make_build

%install
%makeinstall_std
mv %buildroot/%_datadir/doc/%name install-doc

%files
%doc AUTHORS ChangeLog NEWS README THANKS TODO install-doc/*
%_bindir/*
%_man1dir/*
%_man5dir/*
%_man7dir/*

%changelog
* Tue Jul 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.008.09.149-alt2
- Update build for new toolchain

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.008.09.149-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Jun 21 2009 Kirill Maslinsky <kirill@altlinux.org> 1.008.09.149-alt1
- Initial build for ALT Linux Sisyphus

