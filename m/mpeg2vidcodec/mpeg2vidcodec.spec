Name: mpeg2vidcodec
Version: 1.2
Release: alt1

Summary: MPEG-2 Encoder / Decoder 
Summary(ru_RU.UTF-8): MPEG-2 кодер и декодер
License: as-is
Group: Video
URL: http://www.mpeg.org/MPEG/MSSG
Source0: %{name}_v12.tar.gz

%description
This package contains an implementation of an ISO/IEC DIS 13818-2
codec. It converts uncompressed video frames into MPEG-1 and MPEG-2
video coded bitstream sequences, and vice versa.

%description -l ru_RU.UTF-8
Пакет содержит ISO/IEC DIS 13818-2 кодек, позволяющий преобразовывать 
несжатые видеокадры в кодированные последовательности MPEG-1 и MPEG-2 
и наоборот.

%prep
%setup -c -q

%build
cd mpeg2
%make

%install
%__install -d %buildroot%_bindir
%__install mpeg2/src/mpeg2enc/mpeg2encode %buildroot%_bindir
%__install mpeg2/src/mpeg2dec/mpeg2decode %buildroot%_bindir

%files
%_bindir/*
%doc mpeg2/README mpeg2/doc/* mpeg2/src/mpeg2dec/EXAMPLES mpeg2/src/mpeg2dec/IEEE1180 mpeg2/src/mpeg2dec/SPATIAL.DOC

%changelog
* Sun Apr 11 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.2-alt1
- Initial build
