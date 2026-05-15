%define optflags_lto %nil

%define sover1 26
%define libraw1 libraw%sover1
%define sover2 27
%define libraw2 libraw%sover2

Name: libraw-placeholder
Version: 0.0.1
Release: alt1

Summary: Placeholder for libraw
Group: System/Libraries
License: GPL-3.0
Url: http://altlinux.org

BuildRequires: gcc

%description
%{summary}.

%package -n %libraw1
Summary: Placeholder for %libraw1
Group: System/Libraries
%description -n %libraw1
%{summary}.

%package -n %libraw2
Summary: Placeholder for %libraw1
Group: System/Libraries
%description -n %libraw2
%{summary}.

%prep
%setup  -T -c -n %name-%version

%build
%add_optflags -pedantic
echo "void ___some_unused_function_to_fill_libraw_sources___() {}" >libraw-placeholder.c
gcc %optflags -c libraw-placeholder.c -o libraw.o
ld --shared -soname=libraw.so.%{sover1} libraw.o -o libraw.so.%{sover1}
ld --shared -soname=libraw.so.%{sover2} libraw.o -o libraw.so.%{sover2}

%install
mkdir -p %buildroot/%_libdir/
install -m 0644 libraw.so.%{sover1} %buildroot/%_libdir/libraw.so.%{sover1}.%version
install -m 0644 libraw.so.%{sover2} %buildroot/%_libdir/libraw.so.%{sover2}.%version

%files  -n %libraw1
%_libdir/libraw.so.%{sover1}*

%files  -n %libraw2
%_libdir/libraw.so.%{sover2}*

%changelog
* Fri May 15 2026 Sergey V Turchin <zerg@altlinux.org> 0.0.1-alt1
- initial build
