%define _disable_ld_no_undefined 1
%define git 20131223

Summary:	X.org driver for Silicon Motion Cards
Name:		x11-driver-video-siliconmotion
Version:	1.7.7
%if %git
Release:	0.%git.1
Source0:	xf86-video-siliconmotion-%{git}.tar.xz
%else
Release:	2
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-siliconmotion-%{version}.tar.bz2
%endif
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-siliconmotion is
the X.org driver for Silicon Motion Cards.

%prep
%if %git
%setup -qn xf86-video-siliconmotion
%else
%setup -qn xf86-video-siliconmotion-%{version}
%endif
[ -e configure ] || ./autogen.sh

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/siliconmotion_drv.so
%{_mandir}/man4/siliconmotion.*

