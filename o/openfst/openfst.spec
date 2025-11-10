%def_with check

%global soversion 26

%global release_date "July 2018"

%global descr OpenFst is a library for constructing, combining, optimizing,\
and searching weighted finite-state transducers (FSTs). Weighted\
finite-state transducers are automata where each transition has an input\
label, an output label, and a weight. The more familiar finite-state\
acceptor is represented as a transducer with each transition's input and\
output label equal. Finite-state acceptors are used to represent sets\
of strings (specifically, regular or rational sets); finite-state\
transducers are used to represent binary relations between pairs of\
strings (specifically, rational transductions). The weights can be used\
to represent the cost of taking a particular transition.\
\
FSTs have key applications in speech recognition and synthesis, machine\
translation, optical character recognition, pattern matching, string\
processing, machine learning, information extraction and retrieval among\
others. Often a weighted transducer is used to represent a\
probabilistic model (e.g., an n-gram model, pronunciation model). FSTs\
can be optimized by determinization and minimization, models can be\
applied to hypothesis sets (also represented as automata) or cascaded by\
finite-state composition, and the best results can be selected by\
shortest-path algorithms.

Name: openfst
Version: 1.8.4
Release: alt2

Summary: Weighted finite-state transducer library
License: Apache-2.0
Group: System/Libraries
Url: https://www.openfst.org

# https://www.openfst.org/twiki/pub/FST/FstDownload/%name-%version.tar.gz
Source0: %name-%version.tar
# https://www.openfst.org/twiki/pub/Contrib/OpenFstBashComp/openfstbc
Source1: openfstbc

BuildRequires: gcc-c++
BuildRequires: chrpath
BuildRequires: help2man

# Failed to build on the i586
ExcludeArch: %ix86

%description
%descr

%package -n libopenfst%soversion
Summary: Weighted finite-state transducer library
Group: System/Libraries

%description -n libopenfst%soversion
%descr

%package -n libopenfst-devel
Summary: Development files for the %name
Group: Development/C++
Requires: libopenfst%soversion = %EVR

%description -n libopenfst-devel
%summary.
%descr

%package tools
Summary: Tools for the %name
Group: Other
Requires: libopenfst%soversion = %EVR

%description tools
%summary.
%descr

%prep
%setup
cp %SOURCE1 .

%build
%configure \
	--with-libfstdir=%_libdir/fst-%soversion \
	--enable-compact-fsts \
	--enable-compress \
	--enable-const-fsts \
	--enable-linear-fsts \
	--enable-lookahead-fsts \
	--enable-ngram-fsts \
	--disable-python \
	--enable-special \
	--enable-bin \
	--enable-grm
%make_build

%install
%makeinstall_std
export LD_LIBRARY_PATH=%buildroot%_libdir:%buildroot%_libdir/fst-%soversion

# Remove unnecessary libtool files
find %buildroot%_libdir -name '*.la' | xargs rm -f

# Remove unnecessary rpaths
for i in %buildroot%_libdir/lib*.so.*.*.* %buildroot%_libdir/fst-%soversion/*.so %buildroot%_bindir/*;
	do chrpath -d $i ;
done

# Install the bash completion file
mkdir -p %buildroot%_datadir/bash-completion/completions
install -Dpm 0644 openfstbc %buildroot%_datadir/bash-completion/completions/fstmap
for i in arcsort closure compile compose compress concat connect convert \
	determinize difference disambiguate draw encode epsnormalize equal \
	equivalent info intersect invert isomorphic linear loglinearapply \
	minimize print project prune push randgen randmod relabel replace reverse \
	reweight rmepsilon shortestdistance shortestpath symbols synchronize \
	topsort union;
	do ln -s fstmap %buildroot%_datadir/bash-completion/completions/fst$i
done

# Generate man pages
mkdir -p %buildroot%_man1dir
for i in %buildroot%_bindir/*;
	do help2man -N --version-string=%version $i \
	-o %buildroot%_man1dir/$(basename $i).1 || echo "$i: no man"
done

# Fix the date string and remove buildroot paths from the man pages
sed -e '2s/"1" "[[:alpha:]]* [[:digit:]]*"/"1" %release_date/' \
	-e 's,/builddir.*%_bindir/,,g' \
	-i %buildroot%_man1dir/*.1

%check
%make_build check

%files -n libopenfst%soversion
%_libdir/fst-%soversion
%_libdir/libfst.so.%{soversion}*
%_libdir/libfstcompressscript.so.%{soversion}*
%_libdir/libfstconst.so.%{soversion}*
%_libdir/libfstcompact.so.%{soversion}*
%_libdir/libfstfar.so.%{soversion}*
%_libdir/libfstfarscript.so.%{soversion}*
%_libdir/libfstlinearscript.so.%{soversion}*
%_libdir/libfstlookahead.so.%{soversion}*
%_libdir/libfstngram.so.%{soversion}*
%_libdir/libfstpdtscript.so.%{soversion}*
%_libdir/libfstmpdtscript.so.%{soversion}*
%_libdir/libfstscript.so.%{soversion}*
%_libdir/libfstspecial.so.%{soversion}*

%files -n libopenfst-devel
%_libdir/libfst.so
%_libdir/libfstcompressscript.so
%_libdir/libfstcompact.so
%_libdir/libfstconst.so
%_libdir/libfstfar.so
%_libdir/libfstfarscript.so
%_libdir/libfstlinearscript.so
%_libdir/libfstlookahead.so
%_libdir/libfstngram.so
%_libdir/libfstpdtscript.so
%_libdir/libfstscript.so
%_libdir/libfstspecial.so
%_libdir/libfstmpdtscript.so
%_includedir/fst

%files tools
%_bindir/farcompilestrings
%_bindir/farconvert
%_bindir/farcreate
%_bindir/farencode
%_bindir/farequal
%_bindir/farextract
%_bindir/farinfo
%_bindir/farisomorphic
%_bindir/farprintstrings
%_bindir/fstarcsort
%_bindir/fstclosure
%_bindir/fstcompile
%_bindir/fstcompose
%_bindir/fstcompress
%_bindir/fstconcat
%_bindir/fstconnect
%_bindir/fstconvert
%_bindir/fstdeterminize
%_bindir/fstdifference
%_bindir/fstdisambiguate
%_bindir/fstdraw
%_bindir/fstencode
%_bindir/fstepsnormalize
%_bindir/fstequal
%_bindir/fstequivalent
%_bindir/fstinfo
%_bindir/fstintersect
%_bindir/fstinvert
%_bindir/fstisomorphic
%_bindir/fstlinear
%_bindir/fstloglinearapply
%_bindir/fstmap
%_bindir/fstminimize
%_bindir/fstprint
%_bindir/fstproject
%_bindir/fstprune
%_bindir/fstpush
%_bindir/fstrandgen
%_bindir/fstrelabel
%_bindir/fstreplace
%_bindir/fstreverse
%_bindir/fstreweight
%_bindir/fstrmepsilon
%_bindir/fstshortestdistance
%_bindir/fstshortestpath
%_bindir/fstspecial
%_bindir/fstsymbols
%_bindir/fstsynchronize
%_bindir/fsttopsort
%_bindir/fstunion
%_bindir/mpdtcompose
%_bindir/mpdtexpand
%_bindir/mpdtinfo
%_bindir/mpdtreverse
%_bindir/mpdtcompose
%_bindir/pdtcompose
%_bindir/pdtexpand
%_bindir/pdtinfo
%_bindir/pdtreverse
%_bindir/pdtreplace
%_bindir/pdtshortestpath
%_datadir/bash-completion/completions/fstarcsort
%_datadir/bash-completion/completions/fstclosure
%_datadir/bash-completion/completions/fstcompile
%_datadir/bash-completion/completions/fstcompose
%_datadir/bash-completion/completions/fstcompress
%_datadir/bash-completion/completions/fstconcat
%_datadir/bash-completion/completions/fstconnect
%_datadir/bash-completion/completions/fstconvert
%_datadir/bash-completion/completions/fstdeterminize
%_datadir/bash-completion/completions/fstdifference
%_datadir/bash-completion/completions/fstdisambiguate
%_datadir/bash-completion/completions/fstdraw
%_datadir/bash-completion/completions/fstencode
%_datadir/bash-completion/completions/fstepsnormalize
%_datadir/bash-completion/completions/fstequal
%_datadir/bash-completion/completions/fstequivalent
%_datadir/bash-completion/completions/fstinfo
%_datadir/bash-completion/completions/fstintersect
%_datadir/bash-completion/completions/fstinvert
%_datadir/bash-completion/completions/fstisomorphic
%_datadir/bash-completion/completions/fstlinear
%_datadir/bash-completion/completions/fstloglinearapply
%_datadir/bash-completion/completions/fstmap
%_datadir/bash-completion/completions/fstminimize
%_datadir/bash-completion/completions/fstprint
%_datadir/bash-completion/completions/fstproject
%_datadir/bash-completion/completions/fstprune
%_datadir/bash-completion/completions/fstpush
%_datadir/bash-completion/completions/fstrandgen
%_datadir/bash-completion/completions/fstrandmod
%_datadir/bash-completion/completions/fstrelabel
%_datadir/bash-completion/completions/fstreplace
%_datadir/bash-completion/completions/fstreverse
%_datadir/bash-completion/completions/fstreweight
%_datadir/bash-completion/completions/fstrmepsilon
%_datadir/bash-completion/completions/fstshortestdistance
%_datadir/bash-completion/completions/fstshortestpath
%_datadir/bash-completion/completions/fstsymbols
%_datadir/bash-completion/completions/fstsynchronize
%_datadir/bash-completion/completions/fsttopsort
%_datadir/bash-completion/completions/fstunion
%_man1dir/farcompilestrings.1.xz
%_man1dir/farconvert.1.xz
%_man1dir/farcreate.1.xz
%_man1dir/farencode.1.xz
%_man1dir/farequal.1.xz
%_man1dir/farextract.1.xz
%_man1dir/farinfo.1.xz
%_man1dir/farisomorphic.1.xz
%_man1dir/farprintstrings.1.xz
%_man1dir/fstarcsort.1.xz
%_man1dir/fstclosure.1.xz
%_man1dir/fstcompile.1.xz
%_man1dir/fstcompose.1.xz
%_man1dir/fstcompress.1.xz
%_man1dir/fstconcat.1.xz
%_man1dir/fstconnect.1.xz
%_man1dir/fstconvert.1.xz
%_man1dir/fstdeterminize.1.xz
%_man1dir/fstdifference.1.xz
%_man1dir/fstdisambiguate.1.xz
%_man1dir/fstdraw.1.xz
%_man1dir/fstencode.1.xz
%_man1dir/fstepsnormalize.1.xz
%_man1dir/fstequal.1.xz
%_man1dir/fstequivalent.1.xz
%_man1dir/fstinfo.1.xz
%_man1dir/fstintersect.1.xz
%_man1dir/fstinvert.1.xz
%_man1dir/fstisomorphic.1.xz
%_man1dir/fstlinear.1.xz
%_man1dir/fstloglinearapply.1.xz
%_man1dir/fstmap.1.xz
%_man1dir/fstminimize.1.xz
%_man1dir/fstprint.1.xz
%_man1dir/fstproject.1.xz
%_man1dir/fstprune.1.xz
%_man1dir/fstpush.1.xz
%_man1dir/fstrandgen.1.xz
%_man1dir/fstrelabel.1.xz
%_man1dir/fstreplace.1.xz
%_man1dir/fstreverse.1.xz
%_man1dir/fstreweight.1.xz
%_man1dir/fstrmepsilon.1.xz
%_man1dir/fstshortestdistance.1.xz
%_man1dir/fstshortestpath.1.xz
%_man1dir/fstspecial.1.xz
%_man1dir/fstsymbols.1.xz
%_man1dir/fstsynchronize.1.xz
%_man1dir/fsttopsort.1.xz
%_man1dir/fstunion.1.xz
%_man1dir/mpdtcompose.1.xz
%_man1dir/mpdtexpand.1.xz
%_man1dir/mpdtinfo.1.xz
%_man1dir/mpdtreverse.1.xz
%_man1dir/pdtcompose.1.xz
%_man1dir/pdtexpand.1.xz
%_man1dir/pdtinfo.1.xz
%_man1dir/pdtreplace.1.xz
%_man1dir/pdtreverse.1.xz
%_man1dir/pdtshortestpath.1.xz

%changelog
* Mon Nov 10 2025 Ulysses Apokin <ulysses@altlinux.org> 1.8.4-alt2
- Symlink libfst.so moved to -devel package

* Wed Oct 22 2025 Ulysses Apokin <ulysses@altlinux.org> 1.8.4-alt1
- Initial build for Sisyphus.
