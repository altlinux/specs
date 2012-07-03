Name: mcl
Version: 1.008.09.149
Release: alt1

Summary: Markov cluster algorithm for graphs
License: GPLv3
Group: Sciences/Mathematics
Url: http://www.micans.org/mcl

Packager: Kirill Maslinsky <kirill@altlinux.org>
Source0: %name-%version.tar

%description
The MCL algorithm is short for the Markov Cluster Algorithm, a fast and scalable 
unsupervised cluster algorithm for graphs based on simulation of (stochastic) 
flow in graphs. The algorithm was invented/discovered by Stijn van Dongen at the 
Centre for Mathematics and Computer Science (also known as CWI) in the 
Netherlands. 

%prep 
%setup %name-%version.tar

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
* Sun Jun 21 2009 Kirill Maslinsky <kirill@altlinux.org> 1.008.09.149-alt1
- Initial build for ALT Linux Sisyphus

