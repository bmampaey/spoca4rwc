#!/usr/bin/env/python

class _SolarSurface_Area:

    _types_map = {
        'Mm': {'type': float, 'subtype': None},
        'Arcsec': {'type': float, 'subtype': None},
        'SH': {'type': float, 'subtype': None},
        'error': {'type': float, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , Mm=None
            , Arcsec=None
            , SH=None
            , error=None
            ):
        self.Mm = Mm
        self.Arcsec = Arcsec
        self.SH = SH
        self.error = error
    
    def _get_Mm(self):
        return self.__Mm
    def _set_Mm(self, value):
        if not isinstance(value, float):
            raise TypeError("Mm must be float")
        self.__Mm = value
    Mm = property(_get_Mm, _set_Mm)
    
    def _get_Arcsec(self):
        return self.__Arcsec
    def _set_Arcsec(self, value):
        if not isinstance(value, float):
            raise TypeError("Arcsec must be float")
        self.__Arcsec = value
    Arcsec = property(_get_Arcsec, _set_Arcsec)
    
    def _get_SH(self):
        return self.__SH
    def _set_SH(self, value):
        if not isinstance(value, float):
            raise TypeError("SH must be float")
        self.__SH = value
    SH = property(_get_SH, _set_SH)
    
    def _get_error(self):
        return self.__error
    def _set_error(self, value):
        if not isinstance(value, float):
            raise TypeError("error must be float")
        self.__error = value
    error = property(_get_error, _set_error)
    
    def as_dict(self):
        d = dict()
        if self.__Mm is not None:
            d['Mm'] = self.__Mm.as_dict() if hasattr(self.__Mm, 'as_dict') else self.__Mm
        if self.__Arcsec is not None:
            d['Arcsec'] = self.__Arcsec.as_dict() if hasattr(self.__Arcsec, 'as_dict') else self.__Arcsec
        if self.__SH is not None:
            d['SH'] = self.__SH.as_dict() if hasattr(self.__SH, 'as_dict') else self.__SH
        if self.__error is not None:
            d['error'] = self.__error.as_dict() if hasattr(self.__error, 'as_dict') else self.__error
        return d

class FT__SolarSurface_Area:

    _event_type_enum = ['_SolarSurface_Area', ]
    _types_map = {
        'data': {'type': _SolarSurface_Area, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , data=None
            , name=None
            , event_type='_SolarSurface_Area'
            ):
        self.data = data
        self.name = name
        self.event_type = event_type
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, _SolarSurface_Area):
            raise TypeError("data must be _SolarSurface_Area")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum:
            self.__event_type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def as_dict(self):
        d = dict()
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        return d

class CoronalHole:

    _Provider_enum = ['+Provider_Catania', '+Provider_NOAA', '+Provider_USET', '+Provider_UKMO', '+Provider_KSO', ]
    _types_map = {
        'Polarity': {'type': str, 'subtype': None},
        'Detections': {'type': list, 'subtype': None},
        'EndTime': {'type': str, 'subtype': None},
        'BeginTime': {'type': str, 'subtype': None},
        'Provider': {'type': str, 'subtype': None},
    }
    _formats_map = {
        'Polarity': 'date-time',
        'EndTime': 'date-time',
        'BeginTime': 'date-time',
    }

    def __init__(self
            , Polarity=None
            , Detections=None
            , EndTime=None
            , BeginTime=None
            , Provider=None
            ):
        self.Polarity = Polarity
        self.Detections = Detections
        self.EndTime = EndTime
        self.BeginTime = BeginTime
        self.Provider = Provider
    
    def _get_Polarity(self):
        return self.__Polarity
    def _set_Polarity(self, value):
        if not isinstance(value, str):
            raise TypeError("Polarity must be str")
        self.__Polarity = value
    Polarity = property(_get_Polarity, _set_Polarity)
    
    def _get_Detections(self):
        return self.__Detections
    def _set_Detections(self, value):
        if not isinstance(value, list):
            raise TypeError("Detections must be list")
        self.__Detections = value
    Detections = property(_get_Detections, _set_Detections)
    
    def _get_EndTime(self):
        return self.__EndTime
    def _set_EndTime(self, value):
        if not isinstance(value, str):
            raise TypeError("EndTime must be str")
        self.__EndTime = value
    EndTime = property(_get_EndTime, _set_EndTime)
    
    def _get_BeginTime(self):
        return self.__BeginTime
    def _set_BeginTime(self, value):
        if not isinstance(value, str):
            raise TypeError("BeginTime must be str")
        self.__BeginTime = value
    BeginTime = property(_get_BeginTime, _set_BeginTime)
    
    def _get_Provider(self):
        return self.__Provider
    def _set_Provider(self, value):
        if not isinstance(value, str):
            raise TypeError("Provider must be str")
        if value in self._Provider_enum:
            self.__Provider = value
        else:
            raise ValueError("Value {} not in _Provider_enum list".format(value))
    Provider = property(_get_Provider, _set_Provider)
    
    def as_dict(self):
        d = dict()
        if self.__Polarity is not None:
            d['Polarity'] = self.__Polarity.as_dict() if hasattr(self.__Polarity, 'as_dict') else self.__Polarity
        if self.__Detections is not None:
            d['Detections'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Detections]
        if self.__EndTime is not None:
            d['EndTime'] = self.__EndTime.as_dict() if hasattr(self.__EndTime, 'as_dict') else self.__EndTime
        if self.__BeginTime is not None:
            d['BeginTime'] = self.__BeginTime.as_dict() if hasattr(self.__BeginTime, 'as_dict') else self.__BeginTime
        if self.__Provider is not None:
            d['Provider'] = self.__Provider.as_dict() if hasattr(self.__Provider, 'as_dict') else self.__Provider
        return d

class FT_CoronalHole:

    _event_type_enum = ['CoronalHole', ]
    _types_map = {
        'data': {'type': CoronalHole, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , data=None
            , name=None
            , event_type='CoronalHole'
            ):
        self.data = data
        self.name = name
        self.event_type = event_type
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, CoronalHole):
            raise TypeError("data must be CoronalHole")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum:
            self.__event_type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def as_dict(self):
        d = dict()
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        return d

class _HeliographicCoordinate_Stonyhurst:

    _types_map = {
        'Latitude': {'type': float, 'subtype': None},
        'Longitude': {'type': float, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , Latitude=None
            , Longitude=None
            ):
        self.Latitude = Latitude
        self.Longitude = Longitude
    
    def _get_Latitude(self):
        return self.__Latitude
    def _set_Latitude(self, value):
        if not isinstance(value, float):
            raise TypeError("Latitude must be float")
        self.__Latitude = value
    Latitude = property(_get_Latitude, _set_Latitude)
    
    def _get_Longitude(self):
        return self.__Longitude
    def _set_Longitude(self, value):
        if not isinstance(value, float):
            raise TypeError("Longitude must be float")
        self.__Longitude = value
    Longitude = property(_get_Longitude, _set_Longitude)
    
    def as_dict(self):
        d = dict()
        if self.__Latitude is not None:
            d['Latitude'] = self.__Latitude.as_dict() if hasattr(self.__Latitude, 'as_dict') else self.__Latitude
        if self.__Longitude is not None:
            d['Longitude'] = self.__Longitude.as_dict() if hasattr(self.__Longitude, 'as_dict') else self.__Longitude
        return d

class FT__HeliographicCoordinate_Stonyhurst:

    _event_type_enum = ['_HeliographicCoordinate_Stonyhurst', ]
    _types_map = {
        'data': {'type': _HeliographicCoordinate_Stonyhurst, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , data=None
            , name=None
            , event_type='_HeliographicCoordinate_Stonyhurst'
            ):
        self.data = data
        self.name = name
        self.event_type = event_type
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, _HeliographicCoordinate_Stonyhurst):
            raise TypeError("data must be _HeliographicCoordinate_Stonyhurst")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum:
            self.__event_type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def as_dict(self):
        d = dict()
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        return d

class _HeliographicCoordinate_Carrington:

    _types_map = {
        'Latitude': {'type': float, 'subtype': None},
        'Longitude': {'type': float, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , Latitude=None
            , Longitude=None
            ):
        self.Latitude = Latitude
        self.Longitude = Longitude
    
    def _get_Latitude(self):
        return self.__Latitude
    def _set_Latitude(self, value):
        if not isinstance(value, float):
            raise TypeError("Latitude must be float")
        self.__Latitude = value
    Latitude = property(_get_Latitude, _set_Latitude)
    
    def _get_Longitude(self):
        return self.__Longitude
    def _set_Longitude(self, value):
        if not isinstance(value, float):
            raise TypeError("Longitude must be float")
        self.__Longitude = value
    Longitude = property(_get_Longitude, _set_Longitude)
    
    def as_dict(self):
        d = dict()
        if self.__Latitude is not None:
            d['Latitude'] = self.__Latitude.as_dict() if hasattr(self.__Latitude, 'as_dict') else self.__Latitude
        if self.__Longitude is not None:
            d['Longitude'] = self.__Longitude.as_dict() if hasattr(self.__Longitude, 'as_dict') else self.__Longitude
        return d

class FT__HeliographicCoordinate_Carrington:

    _event_type_enum = ['_HeliographicCoordinate_Carrington', ]
    _types_map = {
        'data': {'type': _HeliographicCoordinate_Carrington, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , data=None
            , name=None
            , event_type='_HeliographicCoordinate_Carrington'
            ):
        self.data = data
        self.name = name
        self.event_type = event_type
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, _HeliographicCoordinate_Carrington):
            raise TypeError("data must be _HeliographicCoordinate_Carrington")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum:
            self.__event_type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def as_dict(self):
        d = dict()
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        return d

class _HeliographicCoordinate:

    _types_map = {
        'Carrington': {'type': FT__HeliographicCoordinate_Carrington, 'subtype': None},
        'Stonyhurst': {'type': FT__HeliographicCoordinate_Stonyhurst, 'subtype': None},
        'Time': {'type': str, 'subtype': None},
    }
    _formats_map = {
        'Time': 'date-time',
    }

    def __init__(self
            , Carrington=None
            , Stonyhurst=None
            , Time=None
            ):
        self.Carrington = Carrington
        self.Stonyhurst = Stonyhurst
        self.Time = Time
    
    def _get_Carrington(self):
        return self.__Carrington
    def _set_Carrington(self, value):
        if not isinstance(value, FT__HeliographicCoordinate_Carrington):
            raise TypeError("Carrington must be FT__HeliographicCoordinate_Carrington")
        self.__Carrington = value
    Carrington = property(_get_Carrington, _set_Carrington)
    
    def _get_Stonyhurst(self):
        return self.__Stonyhurst
    def _set_Stonyhurst(self, value):
        if not isinstance(value, FT__HeliographicCoordinate_Stonyhurst):
            raise TypeError("Stonyhurst must be FT__HeliographicCoordinate_Stonyhurst")
        self.__Stonyhurst = value
    Stonyhurst = property(_get_Stonyhurst, _set_Stonyhurst)
    
    def _get_Time(self):
        return self.__Time
    def _set_Time(self, value):
        if not isinstance(value, str):
            raise TypeError("Time must be str")
        self.__Time = value
    Time = property(_get_Time, _set_Time)
    
    def as_dict(self):
        d = dict()
        if self.__Carrington is not None:
            d['Carrington'] = self.__Carrington.as_dict() if hasattr(self.__Carrington, 'as_dict') else self.__Carrington
        if self.__Stonyhurst is not None:
            d['Stonyhurst'] = self.__Stonyhurst.as_dict() if hasattr(self.__Stonyhurst, 'as_dict') else self.__Stonyhurst
        if self.__Time is not None:
            d['Time'] = self.__Time.as_dict() if hasattr(self.__Time, 'as_dict') else self.__Time
        return d

class FT__HeliographicCoordinate:

    _event_type_enum = ['_HeliographicCoordinate', ]
    _types_map = {
        'data': {'type': _HeliographicCoordinate, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , data=None
            , name=None
            , event_type='_HeliographicCoordinate'
            ):
        self.data = data
        self.name = name
        self.event_type = event_type
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, _HeliographicCoordinate):
            raise TypeError("data must be _HeliographicCoordinate")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum:
            self.__event_type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def as_dict(self):
        d = dict()
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        return d

class _SolarSurface_BoundingBox:

    _types_map = {
        'LongitudeW': {'type': float, 'subtype': None},
        'LatitudeS': {'type': float, 'subtype': None},
        'LongitudeE': {'type': float, 'subtype': None},
        'LatitudeN': {'type': float, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , LongitudeW=None
            , LatitudeS=None
            , LongitudeE=None
            , LatitudeN=None
            ):
        self.LongitudeW = LongitudeW
        self.LatitudeS = LatitudeS
        self.LongitudeE = LongitudeE
        self.LatitudeN = LatitudeN
    
    def _get_LongitudeW(self):
        return self.__LongitudeW
    def _set_LongitudeW(self, value):
        if not isinstance(value, float):
            raise TypeError("LongitudeW must be float")
        self.__LongitudeW = value
    LongitudeW = property(_get_LongitudeW, _set_LongitudeW)
    
    def _get_LatitudeS(self):
        return self.__LatitudeS
    def _set_LatitudeS(self, value):
        if not isinstance(value, float):
            raise TypeError("LatitudeS must be float")
        self.__LatitudeS = value
    LatitudeS = property(_get_LatitudeS, _set_LatitudeS)
    
    def _get_LongitudeE(self):
        return self.__LongitudeE
    def _set_LongitudeE(self, value):
        if not isinstance(value, float):
            raise TypeError("LongitudeE must be float")
        self.__LongitudeE = value
    LongitudeE = property(_get_LongitudeE, _set_LongitudeE)
    
    def _get_LatitudeN(self):
        return self.__LatitudeN
    def _set_LatitudeN(self, value):
        if not isinstance(value, float):
            raise TypeError("LatitudeN must be float")
        self.__LatitudeN = value
    LatitudeN = property(_get_LatitudeN, _set_LatitudeN)
    
    def as_dict(self):
        d = dict()
        if self.__LongitudeW is not None:
            d['LongitudeW'] = self.__LongitudeW.as_dict() if hasattr(self.__LongitudeW, 'as_dict') else self.__LongitudeW
        if self.__LatitudeS is not None:
            d['LatitudeS'] = self.__LatitudeS.as_dict() if hasattr(self.__LatitudeS, 'as_dict') else self.__LatitudeS
        if self.__LongitudeE is not None:
            d['LongitudeE'] = self.__LongitudeE.as_dict() if hasattr(self.__LongitudeE, 'as_dict') else self.__LongitudeE
        if self.__LatitudeN is not None:
            d['LatitudeN'] = self.__LatitudeN.as_dict() if hasattr(self.__LatitudeN, 'as_dict') else self.__LatitudeN
        return d

class FT__SolarSurface_BoundingBox:

    _event_type_enum = ['_SolarSurface_BoundingBox', ]
    _types_map = {
        'data': {'type': _SolarSurface_BoundingBox, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , data=None
            , name=None
            , event_type='_SolarSurface_BoundingBox'
            ):
        self.data = data
        self.name = name
        self.event_type = event_type
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, _SolarSurface_BoundingBox):
            raise TypeError("data must be _SolarSurface_BoundingBox")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum:
            self.__event_type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def as_dict(self):
        d = dict()
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        return d

class SPOCA_CoronalHole:

    _types_map = {
        'Skewness': {'type': list, 'subtype': str},
        'Min': {'type': list, 'subtype': str},
        'Max': {'type': list, 'subtype': str},
        'Median': {'type': list, 'subtype': str},
        'ThirdQuartile': {'type': list, 'subtype': str},
        'FirstQuartile': {'type': list, 'subtype': str},
        'Var': {'type': list, 'subtype': str},
        'DetectionTime': {'type': str, 'subtype': None},
        'Kurtosis': {'type': list, 'subtype': str},
        'Mean': {'type': list, 'subtype': str},
    }
    _formats_map = {
        'DetectionTime': 'date-time',
    }

    def __init__(self
            , Skewness=None
            , Min=None
            , Max=None
            , Median=None
            , ThirdQuartile=None
            , FirstQuartile=None
            , Var=None
            , DetectionTime=None
            , Kurtosis=None
            , Mean=None
            ):
        self.Skewness = Skewness
        self.Min = Min
        self.Max = Max
        self.Median = Median
        self.ThirdQuartile = ThirdQuartile
        self.FirstQuartile = FirstQuartile
        self.Var = Var
        self.DetectionTime = DetectionTime
        self.Kurtosis = Kurtosis
        self.Mean = Mean
    
    def _get_Skewness(self):
        return self.__Skewness
    def _set_Skewness(self, value):
        if not isinstance(value, list):
            raise TypeError("Skewness must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("Skewness list values must be str")
        self.__Skewness = value
    Skewness = property(_get_Skewness, _set_Skewness)
    
    def _get_Min(self):
        return self.__Min
    def _set_Min(self, value):
        if not isinstance(value, list):
            raise TypeError("Min must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("Min list values must be str")
        self.__Min = value
    Min = property(_get_Min, _set_Min)
    
    def _get_Max(self):
        return self.__Max
    def _set_Max(self, value):
        if not isinstance(value, list):
            raise TypeError("Max must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("Max list values must be str")
        self.__Max = value
    Max = property(_get_Max, _set_Max)
    
    def _get_Median(self):
        return self.__Median
    def _set_Median(self, value):
        if not isinstance(value, list):
            raise TypeError("Median must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("Median list values must be str")
        self.__Median = value
    Median = property(_get_Median, _set_Median)
    
    def _get_ThirdQuartile(self):
        return self.__ThirdQuartile
    def _set_ThirdQuartile(self, value):
        if not isinstance(value, list):
            raise TypeError("ThirdQuartile must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("ThirdQuartile list values must be str")
        self.__ThirdQuartile = value
    ThirdQuartile = property(_get_ThirdQuartile, _set_ThirdQuartile)
    
    def _get_FirstQuartile(self):
        return self.__FirstQuartile
    def _set_FirstQuartile(self, value):
        if not isinstance(value, list):
            raise TypeError("FirstQuartile must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("FirstQuartile list values must be str")
        self.__FirstQuartile = value
    FirstQuartile = property(_get_FirstQuartile, _set_FirstQuartile)
    
    def _get_Var(self):
        return self.__Var
    def _set_Var(self, value):
        if not isinstance(value, list):
            raise TypeError("Var must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("Var list values must be str")
        self.__Var = value
    Var = property(_get_Var, _set_Var)
    
    def _get_DetectionTime(self):
        return self.__DetectionTime
    def _set_DetectionTime(self, value):
        if not isinstance(value, str):
            raise TypeError("DetectionTime must be str")
        self.__DetectionTime = value
    DetectionTime = property(_get_DetectionTime, _set_DetectionTime)
    
    def _get_Kurtosis(self):
        return self.__Kurtosis
    def _set_Kurtosis(self, value):
        if not isinstance(value, list):
            raise TypeError("Kurtosis must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("Kurtosis list values must be str")
        self.__Kurtosis = value
    Kurtosis = property(_get_Kurtosis, _set_Kurtosis)
    
    def _get_Mean(self):
        return self.__Mean
    def _set_Mean(self, value):
        if not isinstance(value, list):
            raise TypeError("Mean must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("Mean list values must be str")
        self.__Mean = value
    Mean = property(_get_Mean, _set_Mean)
    
    def as_dict(self):
        d = dict()
        if self.__Skewness is not None:
            d['Skewness'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Skewness]
        if self.__Min is not None:
            d['Min'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Min]
        if self.__Max is not None:
            d['Max'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Max]
        if self.__Median is not None:
            d['Median'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Median]
        if self.__ThirdQuartile is not None:
            d['ThirdQuartile'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__ThirdQuartile]
        if self.__FirstQuartile is not None:
            d['FirstQuartile'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__FirstQuartile]
        if self.__Var is not None:
            d['Var'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Var]
        if self.__DetectionTime is not None:
            d['DetectionTime'] = self.__DetectionTime.as_dict() if hasattr(self.__DetectionTime, 'as_dict') else self.__DetectionTime
        if self.__Kurtosis is not None:
            d['Kurtosis'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Kurtosis]
        if self.__Mean is not None:
            d['Mean'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Mean]
        return d

class FT_SPOCA_CoronalHole:

    _event_type_enum = ['SPOCA_CoronalHole', ]
    _types_map = {
        'data': {'type': SPOCA_CoronalHole, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , data=None
            , name=None
            , event_type='SPOCA_CoronalHole'
            ):
        self.data = data
        self.name = name
        self.event_type = event_type
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, SPOCA_CoronalHole):
            raise TypeError("data must be SPOCA_CoronalHole")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum:
            self.__event_type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def as_dict(self):
        d = dict()
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        return d

class CoronalHoleDetection:

    _Provider_enum = ['+Provider_Catania', '+Provider_NOAA', '+Provider_USET', '+Provider_UKMO', '+Provider_KSO', ]
    _types_map = {
        'Area': {'type': FT__SolarSurface_Area, 'subtype': None},
        'CoronalHole': {'type': list, 'subtype': None},
        'Location': {'type': FT__HeliographicCoordinate, 'subtype': None},
        'Provider': {'type': str, 'subtype': None},
        'BoundingBox': {'type': FT__SolarSurface_BoundingBox, 'subtype': None},
        'Contour': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , Area=None
            , CoronalHole=None
            , Location=None
            , Provider=None
            , BoundingBox=None
            , Contour=None
            ):
        self.Area = Area
        self.CoronalHole = CoronalHole
        self.Location = Location
        self.Provider = Provider
        self.BoundingBox = BoundingBox
        self.Contour = Contour
    
    def _get_Area(self):
        return self.__Area
    def _set_Area(self, value):
        if not isinstance(value, FT__SolarSurface_Area):
            raise TypeError("Area must be FT__SolarSurface_Area")
        self.__Area = value
    Area = property(_get_Area, _set_Area)
    
    def _get_CoronalHole(self):
        return self.__CoronalHole
    def _set_CoronalHole(self, value):
        if not isinstance(value, list):
            raise TypeError("CoronalHole must be list")
        self.__CoronalHole = value
    CoronalHole = property(_get_CoronalHole, _set_CoronalHole)
    
    def _get_Location(self):
        return self.__Location
    def _set_Location(self, value):
        if not isinstance(value, FT__HeliographicCoordinate):
            raise TypeError("Location must be FT__HeliographicCoordinate")
        self.__Location = value
    Location = property(_get_Location, _set_Location)
    
    def _get_Provider(self):
        return self.__Provider
    def _set_Provider(self, value):
        if not isinstance(value, str):
            raise TypeError("Provider must be str")
        if value in self._Provider_enum:
            self.__Provider = value
        else:
            raise ValueError("Value {} not in _Provider_enum list".format(value))
    Provider = property(_get_Provider, _set_Provider)
    
    def _get_BoundingBox(self):
        return self.__BoundingBox
    def _set_BoundingBox(self, value):
        if not isinstance(value, FT__SolarSurface_BoundingBox):
            raise TypeError("BoundingBox must be FT__SolarSurface_BoundingBox")
        self.__BoundingBox = value
    BoundingBox = property(_get_BoundingBox, _set_BoundingBox)
    
    def _get_Contour(self):
        return self.__Contour
    def _set_Contour(self, value):
        if not isinstance(value, list):
            raise TypeError("Contour must be list")
        self.__Contour = value
    Contour = property(_get_Contour, _set_Contour)
    
    def as_dict(self):
        d = dict()
        if self.__Area is not None:
            d['Area'] = self.__Area.as_dict() if hasattr(self.__Area, 'as_dict') else self.__Area
        if self.__CoronalHole is not None:
            d['CoronalHole'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__CoronalHole]
        if self.__Location is not None:
            d['Location'] = self.__Location.as_dict() if hasattr(self.__Location, 'as_dict') else self.__Location
        if self.__Provider is not None:
            d['Provider'] = self.__Provider.as_dict() if hasattr(self.__Provider, 'as_dict') else self.__Provider
        if self.__BoundingBox is not None:
            d['BoundingBox'] = self.__BoundingBox.as_dict() if hasattr(self.__BoundingBox, 'as_dict') else self.__BoundingBox
        if self.__Contour is not None:
            d['Contour'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Contour]
        return d

class FT_CoronalHoleDetection:

    _event_type_enum = ['CoronalHoleDetection', ]
    _types_map = {
        'data': {'type': CoronalHoleDetection, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , data=None
            , name=None
            , event_type='CoronalHoleDetection'
            ):
        self.data = data
        self.name = name
        self.event_type = event_type
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, CoronalHoleDetection):
            raise TypeError("data must be CoronalHoleDetection")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum:
            self.__event_type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def as_dict(self):
        d = dict()
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        return d

class _CoronalHoleDetection__SPOCA_CoronalHole_:

    _types_map = {
        'SPOCA_CoronalHole': {'type': list, 'subtype': None},
        'CoronalHoleDetection': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , SPOCA_CoronalHole=None
            , CoronalHoleDetection=None
            ):
        self.SPOCA_CoronalHole = SPOCA_CoronalHole
        self.CoronalHoleDetection = CoronalHoleDetection
    
    def _get_SPOCA_CoronalHole(self):
        return self.__SPOCA_CoronalHole
    def _set_SPOCA_CoronalHole(self, value):
        if not isinstance(value, list):
            raise TypeError("SPOCA_CoronalHole must be list")
        self.__SPOCA_CoronalHole = value
    SPOCA_CoronalHole = property(_get_SPOCA_CoronalHole, _set_SPOCA_CoronalHole)
    
    def _get_CoronalHoleDetection(self):
        return self.__CoronalHoleDetection
    def _set_CoronalHoleDetection(self, value):
        if not isinstance(value, list):
            raise TypeError("CoronalHoleDetection must be list")
        self.__CoronalHoleDetection = value
    CoronalHoleDetection = property(_get_CoronalHoleDetection, _set_CoronalHoleDetection)
    
    def as_dict(self):
        d = dict()
        if self.__SPOCA_CoronalHole is not None:
            d['SPOCA_CoronalHole'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__SPOCA_CoronalHole]
        if self.__CoronalHoleDetection is not None:
            d['CoronalHoleDetection'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__CoronalHoleDetection]
        return d

class FT__CoronalHoleDetection__SPOCA_CoronalHole_:

    _event_type_enum = ['_CoronalHoleDetection__SPOCA_CoronalHole_', ]
    _types_map = {
        'data': {'type': _CoronalHoleDetection__SPOCA_CoronalHole_, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , data=None
            , name=None
            , event_type='_CoronalHoleDetection__SPOCA_CoronalHole_'
            ):
        self.data = data
        self.name = name
        self.event_type = event_type
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, _CoronalHoleDetection__SPOCA_CoronalHole_):
            raise TypeError("data must be _CoronalHoleDetection__SPOCA_CoronalHole_")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum:
            self.__event_type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def as_dict(self):
        d = dict()
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        return d

class RootObject:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
            ):
        pass
    
    def as_dict(self):
        d = dict()
        return d
