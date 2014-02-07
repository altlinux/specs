Name: multicat
Version: 2.0
Release: alt1
Summary: A set of tools designed to manipulate multicast streams
License: GPLv2+
Group: Video
Url: http://www.videolan.org/projects/multicat.html

Source: %name-%version.tar

BuildRequires: libdvbpsi-devel bitstream-headers

%description 
The multicat package contains a set of tools designed to easily and efficiently
manipulate multicast streams in general, and MPEG-2 Transport Streams (ISO/IEC
13818-1) in particular.

The multicat tool itself is a 1 input/1 output application. Inputs and outputs
can be network streams (unicast and multicast), files, character devices or
FIFOs.

Multicat tries to rebuild the internal clock of the input stream; but it wants
to remain agnostic of what is transported, so in case of files the said clock
is stored to an auxiliary file (example.aux accompanies example.ts) while
recording. Other inputs are considered "live", and the input clock is simply
derived from the reception time of the packets.

IngesTS is a companion application designed to manipulate TS files. It reads
the PCR values of the file, and builds the auxiliary file that is necessary for
multicat.

OffseTS is another companion application to manipulate auxiliary files.  Given
an offset in time from the beginning of the file, it returns the offset of the
position in number of packets.

Finally aggregaRTP and desaggregaRTP can be used to carry a high-bitrate signal
over several contribution links.

The multicat suite of applications is very lightweight and designed to operate
in tight environments. Memory and CPU usages are kept to a minimum, and they
feature only one thread of execution.

%prep
%setup

%build
%make

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
install -pm755 {multicat,ingests,aggregartp,reordertp,offsets,lasts,multicat_validate} %buildroot%_bindir/
install -pm644 {multicat.1,ingests.1,aggregartp.1,reordertp.1,offsets.1,lasts.1} %buildroot%_man1dir/

%files 
%doc COPYING README INSTALL Changelog AUTHORS
%_bindir/*
%_man1dir/*

%changelog
* Thu Feb 06 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0-alt1
- New version

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Mar 01 2010 Konstantin Pavlov <thresh@altlinux.org> 1.0-alt1
- Initial build for ALT Linux Sisyphus.
