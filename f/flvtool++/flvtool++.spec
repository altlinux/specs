Name: flvtool++
Version: 1.2.1
Release: alt1

Summary: flvtool++ is a tool for hinting and manipulating the metadata of Macromedia Flash Video (FLV) files
Summary(ru_RU.UTF8): flvtool++ утилита для манипуляций с метаданными файлов Macromedia Flash Video (FLV)
License: BSD 
Group: File tools
Url: http://mirror.facebook.net/facebook/flvtool++/

Packager: Sergey Alembekov <rt@altlinux.ru>
Source: %name-%version.tar

BuildRequires: scons gcc gcc-c++ boost-devel

%description
flvtool++ is a tool for hinting and manipulating the metadata of
Macromedia Flash Video (FLV) files. It was originally created for
Facebook's Video project (http://facebook.com/video/) for fast video
hinting. It is loosely based on the Ruby FLVTool2, but is written in
C++ for performance reasons.

%description -l ru_RU.UTF8
flvtool++ утилита для манипуляций с Macromedia Flash Video files (FLV).
Она может работать с множеством метаданных. Изначально была создана  для
видео-проекта Facebook и базируется на FLVTool2, но переписана с Ruby на
C++ для повышения производительности.

%prep
%setup -q

%build
scons

%install
%__mkdir_p %buildroot%_bindir 
%__install %name %buildroot%_bindir/

%files
%doc CHANGELOG LICENSE README
%_bindir/*

%changelog
* Wed Dec 23 2009 Sergey Alembekov <rt@altlinux.ru> 1.2.1-alt1
- initial build 


